import pyjoycon as pyjc
from buttons import Buttons
from sticks import Stick
from motion import Motion
from time import sleep


class CombinedJoycon(pyjc.GyroTrackingJoyCon, pyjc.ButtonEventJoyCon):
    def get_stick(self):
        if self.is_left():
            return (self.get_stick_left_horizontal(), self.get_stick_left_vertical())
        else:
            return (self.get_stick_right_horizontal(), self.get_stick_right_vertical())


class Joycons:
    def __init__(self, config):
        self.left = Joycon("left", config["left"])
        self.right = Joycon("right", config["right"])

        self.motion = Motion(config["motion"])

        self.joycon_r = None
        self.joycon_l = None

    def try_reconnect_r(self):
        try:
            joycon_id = pyjc.get_R_id()
            self.joycon_r = CombinedJoycon(*joycon_id, track_sticks=True)
            sleep(0.1)
            self.joycon_r.set_player_lamp(1)
        except ValueError:
            pass

    def try_reconnect_l(self):
        try:
            joycon_id = pyjc.get_L_id()
            self.joycon_l = CombinedJoycon(*joycon_id, track_sticks=True)
            sleep(0.1)
            self.joycon_l.set_player_lamp(1)
        except ValueError:
            pass

    def process(self):
        if self.joycon_l is not None:
            self.left.stick.process(self.joycon_l)
            self.left.buttons.process(self.joycon_l, self.motion)
            if self.motion.side == "left":
                self.motion.process(self.joycon_l)
        else:
            self.try_reconnect_l()

        if self.joycon_r is not None:
            self.right.buttons.process(self.joycon_r, self.motion)
            self.right.stick.process(self.joycon_r)
            if self.motion.side == "right":
                self.motion.process(self.joycon_r)
        else:
            self.try_reconnect_r()


class Joycon:
    def __init__(self, side, config, motion=None):
        self.stick = Stick(config["analog-stick"], side)
        self.buttons = Buttons(config["buttons"])
