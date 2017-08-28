import logging
import os.path as op
import time

import paths
import Tests
from Devices import Devices
from Profilers import Profilers
from Scripts import Scripts
from util import ConfigError, makedirs


class Experiment(object):
    def __init__(self, config):
        self.logger = logging.getLogger(self.__class__.__name__)
        self.basedir = None
        if 'devices' not in config:
            raise ConfigError('"device" is required in the configuration')
        adb_path = config.get('adb_path', 'adb')
        self.devices = Devices(config['devices'], adb_path=adb_path)
        self.replications = Tests.is_integer(config.get('replications', 1))
        self.paths = config.get('paths', [])
        self.profilers = Profilers(config.get('profilers', {}))
        monkeyrunner_path = config.get('monkeyrunner_path', 'monkeyrunner')
        self.scripts = Scripts(config.get('scripts', {}), monkeyrunner_path=monkeyrunner_path)
        self.time_between_run = Tests.is_integer(config.get('time_between_run', 0))
        Tests.check_dependencies(self.devices, self.profilers.dependencies())
        self.output_root = paths.OUTPUT_DIR

    def prepare(self, device):
        self.logger.info('Device: %s' % device)
        self.profilers.load(device)
        device.unplug()

    def cleanup(self, device):
        device.plug()
        self.profilers.stop_profiling(device)
        self.profilers.unload(device)

    def start(self):
        for device in self.devices:
            try:
                paths.OUTPUT_DIR = op.join(self.output_root, 'data/', device.name)
                makedirs(paths.OUTPUT_DIR)
                self.prepare(device)
                self.before_experiment(device)
                for path in self.paths:
                    self.before_first_run(device, path)
                    for run in range(self.replications):
                        self.before_run(device, path, run)
                        self.start_profiling(device, path, run)
                        self.interaction(device, path, run)
                        self.stop_profiling(device, path, run)
                        self.after_run(device, path, run)
                    self.after_last_run(device, path)
                self.after_experiment(device)
            except Exception, e:
                import traceback
                print(traceback.format_exc())
                self.logger.error('%s: %s' % (e.__class__.__name__, e.message))
            finally:
                self.cleanup(device)

    def before_experiment(self, device):
        self.scripts.run('before_experiment', device)

    def before_first_run(self, device, path):
        pass

    def before_run(self, device, path, run):
        self.logger.info('Run %s of %s' % (run + 1, self.replications))
        self.scripts.run('before_run', device)

    def start_profiling(self, device, path, run):
        self.profilers.start_profiling(device)

    def interaction(self, device, path, run):
        self.scripts.run('interaction', device)

    def stop_profiling(self, device, path, run):
        self.profilers.stop_profiling(device)

    def after_run(self, device, path, run):
        self.scripts.run('after_run', device)
        self.profilers.collect_results(device)
        self.logger.debug('Sleeping for %s milliseconds' % self.time_between_run)
        time.sleep(self.time_between_run / 1000.0)

    def after_last_run(self, device, path):
        pass

    def after_experiment(self, device):
        self.logger.info('Experiment completed, start cleanup')
        self.scripts.run('after_experiment', device)
