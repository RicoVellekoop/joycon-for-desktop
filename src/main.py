from time import sleep

from joycon import Joycons

from misc import load_config, app_config

REFRESH_SPEED = app_config["refresh-speed"]
PATH_CONFIG = app_config["path-config"]

config = load_config(PATH_CONFIG)

joycons = Joycons(config)

while True:
    joycons.process()

    sleep(REFRESH_SPEED)
