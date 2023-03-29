from time import sleep
from pyjoycon import JoyCon, get_R_id, get_L_id

from buttons import ButtonHandler
from sticks import StickHandler

from misc import load_config, app_config

REFRESH_SPEED = app_config["refresh-speed"]
PATH_CONFIG = app_config["path-config"]

buttons, sticks = load_config(PATH_CONFIG)
button_handler = ButtonHandler(buttons)
stick_handler = StickHandler(sticks)

joycon_r_id = get_R_id()
joycon_r = JoyCon(*joycon_r_id)
joycon_l_id = get_L_id()
joycon_l = JoyCon(*joycon_l_id)

joycon_r.set_player_lamp(1)
joycon_l.set_player_lamp(1)


while True:
    r_status = joycon_r.get_status()
    l_status = joycon_l.get_status()

    button_handler.process(r_status["buttons"], "right")
    button_handler.process(l_status["buttons"], "left")

    stick_handler.process_right(r_status["analog-sticks"]["right"])
    stick_handler.process_left(l_status["analog-sticks"]["left"])

    sleep(REFRESH_SPEED)
