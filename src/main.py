from time import sleep

from joycon import Joycons

from misc import REFRESH_SPEED, PATH_CONFIG, load_config

config = load_config(PATH_CONFIG)

joycons = Joycons(config)

while True:
    joycons.process()

    sleep(REFRESH_SPEED)
