from math import sqrt
from time import sleep
import mouse as ms

SPEED = 0.25


class Motion:
    def __init__(self, config):
        self.side = config["side"]
        self.sensitivity = config["sensitivity"]
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
            1920 / 2 + controller.pointer.x * 1920 * self.sensitivity,
            1080 / 2 - controller.pointer.y * 1080 * self.sensitivity,
        )
        current_x, current_y = ms.get_position()
        x_dist, y_dist = current_x - x, current_y - y
        if sqrt(x_dist**2 + y_dist**2) < 8:
            return

        ms.move(
            current_x - (x_dist * SPEED),
            current_y - (y_dist * SPEED),
        )

    def toggle(self):
        self.active = not self.active
        if not self.active:
            self.calibrated = False
