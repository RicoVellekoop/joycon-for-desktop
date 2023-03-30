from math import sqrt
from time import sleep
import mouse as ms

from misc import SCREEN_WIDTH, SCREEN_HEIGHT


class Motion:
    def __init__(self, config):
        self.side = config["side"]
        self.sensitivity = config["sensitivity"]
        self.smoothing_factor = config["smoothing"]
        self.min_distance = config["min-distance"]
        self.active = False
        self.calibrated = False

    def process(self, controller):
        if not self.active:
            return
        if not self.calibrated:
            controller.reset_orientation()
            controller.calibrate(seconds=1)
            sleep(1)
            self.calibrated = True
        if controller.pointer is None:
            return
        x, y = (
            SCREEN_WIDTH / 2 + controller.pointer.x * SCREEN_WIDTH * self.sensitivity,
            SCREEN_HEIGHT / 2 - controller.pointer.y * SCREEN_HEIGHT * self.sensitivity,
        )
        current_x, current_y = ms.get_position()
        x_dist, y_dist = current_x - x, current_y - y
        if sqrt(x_dist**2 + y_dist**2) < self.min_distance:
            return

        ms.move(
            current_x - (x_dist * self.smoothing_factor),
            current_y - (y_dist * self.smoothing_factor),
        )

    def toggle(self):
        self.active = not self.active
        if not self.active:
            self.calibrated = False
