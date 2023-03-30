# from time import sleep
# from pyjoycon import JoyCon, get_R_id

# from pprint import pprint
import mouse as ms

# REFRESH_SPEED = 0.01
# CALIBRATE_POINTS = {"first": {"x": 0.0, "y": 0.0}, "second": {"x": 1920, "y": 1080}}
# calibration = {
#     "first": {"x": 0.0, "y": 0.0, "z": 0.0},
#     "second": {"x": 0.0, "y": 0.0, "z": 0.0},
# }


# joycon_r_id = get_R_id()
# joycon_r = JoyCon(*joycon_r_id)

# joycon_r.set_player_lamp(1)


# def setup():
#     global calibration

#     input("Please move the cursor to the first calibration point and press enter: ")
#     r_status = joycon_r.get_status()
#     calibration["first"] = r_status["accel"]

#     input("Please move the cursor to the second calibration point and press enter: ")
#     r_status = joycon_r.get_status()
#     calibration["second"] = r_status["accel"]


# setup()


# def rotation_to_mouse(accel):
#     global calibration

#     x = accel["x"]
#     y = accel["y"]
#     z = accel["z"]

#     x1 = calibration["first"]["x"]
#     y1 = calibration["first"]["y"]
#     z1 = calibration["first"]["z"]

#     x2 = calibration["second"]["x"]
#     y2 = calibration["second"]["y"]
#     z2 = calibration["second"]["z"]

#     x = (x - x1) / (x2 - x1) * 1920
#     y = (y - y1) / (y2 - y1) * 1080

#     return {"x": x, "y": y, "z": z}


# # def gyro_to_mouse(gyro):
# #     global calibration

# #     x = gyro["x"]
# #     y = gyro["y"]
# #     z = gyro["z"]

# #     x1 = calibration["first"]["x"]
# #     y1 = calibration["first"]["y"]

# #     x2 = calibration["second"]["x"]
# #     y2 = calibration["second"]["y"]

# #     x =
# #     y =

# #     return {"x": x, "y": y, "z": z}


# while True:
#     r_status = joycon_r.get_status()
#     ptr = rotation_to_mouse(r_status["accel"])
#     pprint(ptr)
#     ms.move(ptr["x"], ptr["y"])

#     sleep(REFRESH_SPEED)

from pyjoycon import GyroTrackingJoyCon, get_R_id
import time

joycon_id = get_R_id()
joycon = GyroTrackingJoyCon(*joycon_id)
while True:
    print("joycon pointer:  ", joycon.pointer)
    print("joycon rotation: ", joycon.rotation)
    print("joycon direction:", joycon.direction)
    print()

    ms.move(1000 + joycon.pointer[0] * 1920, 200 - joycon.pointer[1] * 1080, 0.2)
    time.sleep(0.05)
