import keyboard as kb
import mouse as ms


class Buttons:
    def __init__(self, config):
        self.config = {
            button: Key(bind)
            for (button, bind) in config.items()
            if bind not in ("_", None)
        }

    def process(self, controller, motion):
        for button, status in controller.events():
            if button not in self.config:
                continue
            if status == 0 and self.config[button].bind != "toggle-motion":
                self.config[button].release()
            elif status == 1 and self.config[button].bind != "toggle-motion":
                self.config[button].press()
            elif status == 1 and self.config[button].bind == "toggle-motion":
                motion.toggle()


def is_mouse_button(bind):
    return bind.startswith("mouse")


class Key:
    def __init__(self, bind):
        self.bind = bind
        self.is_mouse_button = is_mouse_button(bind)

    def press(self):
        if self.is_mouse_button:
            self.mouse_press()
        else:
            try:
                kb.press(self.bind)
            except ValueError:
                raise ValueError(f"Invalid key: {self.bind}")

    def mouse_press(self):
        if self.bind == "mouse-left":
            ms.press("left")
        elif self.bind == "mouse-right":
            ms.press("right")
        elif self.bind == "mouse-middle":
            ms.press("middle")
        else:
            raise ValueError("Invalid mouse button")

    def release(self):
        if self.is_mouse_button:
            self.mouse_release()
        else:
            try:
                kb.release(self.bind)
            except ValueError:
                raise ValueError(f"Invalid key: {self.bind}")

    def mouse_release(self):
        if self.bind == "mouse-left":
            ms.release("left")
        elif self.bind == "mouse-right":
            ms.release("right")
        elif self.bind == "mouse-middle":
            ms.release("middle")
        else:
            raise ValueError("Invalid mouse button")
