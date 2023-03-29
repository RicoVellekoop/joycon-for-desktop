from misc import normalise_stick
import mouse as ms


class StickHandler:
    def __init__(self, config):
        mode, mode_config = config["left"].popitem()
        self.left = {"mode": mode, "config": mode_config}

        mode, mode_config = config["right"].popitem()
        self.right = {"mode": mode, "config": mode_config}

    def process_left(self, controller):
        if self.left["mode"] == "wheel":
            self.process_wheel(controller, self.left["config"], side="left")
        elif self.left["mode"] == "mouse":
            self.process_mouse(controller, self.left["config"], side="left")
        else:
            raise ValueError("Invalid stick mode")

    def process_right(self, controller):
        if self.right["mode"] == "wheel":
            self.process_wheel(controller, self.right["config"], side="right")
        elif self.right["mode"] == "mouse":
            self.process_mouse(controller, self.right["config"], side="right")
        else:
            raise ValueError("Invalid stick mode")

    def process_wheel(self, controller, config, side):
        x, y = normalise_stick(controller, side)
        if config["scroll_direction"] == "horizontal":
            x = x * config["scroll_speed"]
            if round(x) != 0:
                ms.wheel(x)
        elif config["scroll_direction"] == "vertical":
            y = y * config["scroll_speed"]
            if round(y) != 0:
                ms.wheel(-y * config["scroll_speed"])
        else:
            raise ValueError("Invalid scroll direction")

    def process_mouse(self, controller, config, side):
        x, y = normalise_stick(controller, side)
        ms.move(x * config["mouse_speed"], y * config["mouse_speed"], absolute=False)
