import logging

logger = logging.getLogger(__name__)


def main(device, *args, **kwargs):
    print('=INTERACTION=')
    print((device.id))
    print((device.current_activity()))
