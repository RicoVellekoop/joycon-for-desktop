from time import sleep
from pyjoycon import JoyCon, get_R_id, get_L_id


joycon_r_id = get_R_id()
joycon_r = JoyCon(*joycon_r_id)
joycon_l_id = get_L_id()
joycon_l = JoyCon(*joycon_l_id)


while True:
    r_status = joycon_r.get_status()["analog-sticks"]["right"]
    l_status = joycon_l.get_status()["analog-sticks"]["left"]

    print(f"left: {l_status}, right: {r_status}")

    sleep(0.01)
