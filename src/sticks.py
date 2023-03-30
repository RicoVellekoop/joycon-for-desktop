from misc import normalise_stick
import mouse as ms


class Stick:
    def __init__(self, config, side):
        self.mode, self.config = config.popitem()
        self.side = side

    def process(self, controller):
        if self.mode == "wheel":
            self.process_wheel(controller)
        elif self.mode == "mouse":
            self.process_mouse(controller)
        else:
            raise ValueError("Invalid stick mode")

    def process_wheel(self, controller):
        x, y = normalise_stick(controller.get_stick(), self.side)
        if self.config["scroll_direction"] == "horizontal":
            x = x * self.config["scroll_speed"]
            if round(x) != 0:
                ms.wheel(x)
        elif self.config["scroll_direction"] == "vertical":
            y = y * self.config["scroll_speed"]
            if round(y) != 0:
                ms.wheel(-y * self.config["scroll_speed"])
        else:
            raise ValueError("Invalid scroll direction")

    def process_mouse(self, controller):
        x, y = normalise_stick(controller.get_stick(), self.side)
        if round(x) == 0 and round(y) == 0:
            return
        ms.move(
            x * self.config["mouse_speed"],
            y * self.config["mouse_speed"],
            absolute=False,
        )
