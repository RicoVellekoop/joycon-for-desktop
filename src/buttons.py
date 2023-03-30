import keyboard as kb
import mouse as ms


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


SHARED_KEYS = {
    "left": ["minus", "capture", "l-stick"],
    "right": ["plus", "home", "r-stick"],
}


class ButtonHandler:
    def __init__(self, config):
        self.buttons = {
            part: {
                button: {"bind": Key(bind), "is_pressed": False}
                for (button, bind) in buttons.items()
                if bind not in ("_", None)
            }
            for (part, buttons) in config.items()
        }

    def process(self, controller, side):
        for part, buttons in self.buttons.items():
            if part == "shared" or part == side:
                for button, bind in buttons.items():
                    if part == side or (
                        part == "shared" and button in SHARED_KEYS[side]
                    ):
                        if controller[part][button] and not bind["is_pressed"]:
                            bind["bind"].press()
                            bind["is_pressed"] = True
                        elif not controller[part][button] and bind["is_pressed"]:
                            bind["bind"].release()
                            bind["is_pressed"] = False
