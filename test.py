import os,glob
import os.path as op
import zipfile
from AndroidRunner.util import ConfigError

base_path = 'C:\\Users\\LucienPersonal\\Source\\Repos\\androidrunner\\android-runner\\experiments\\apps\\'

xapk_path = base_path + 'tv.twitch.android.app.xapk'

#get extension filename
extension = op.splitext(xapk_path)[-1].lower()

if extension == '.xapk':
    # get path of directory apks will be unzipped into.
    path_apks_to_be_installed = op.splitext(xapk_path)[0].lower()

    with zipfile.ZipFile(xapk_path, 'r') as zip_ref:
        if not op.exists(path_apks_to_be_installed):
            os.makedirs(path_apks_to_be_installed)
        zip_ref.extractall(path_apks_to_be_installed)

    apk_files = glob.glob('*.apk')

    if not apk_files:
        raise ConfigError('No apks found in xapk')

    
    apk_files_paths = [op.join(path_apks_to_be_installed, apk_file) for apk_file in apk_files]

    apk_install_args = ' '.join(apk_files_paths)

    print(apk_install_args)