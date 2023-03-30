import yaml
from yaml.loader import SafeLoader


def load_settings(path="settings.yaml"):
    with open(path) as f:
        settings = yaml.load(f, Loader=SafeLoader)
        return settings["app"], settings["joystick"]


app_config, stick_config = load_settings()

REFRESH_SPEED = app_config["refresh-speed"]
PATH_CONFIG = app_config["path-config"]

SCREEN_WIDTH = app_config["screen"]["width"]
SCREEN_HEIGHT = app_config["screen"]["height"]

L_DEADZONE = stick_config["left"]["deadzone"]
L_HORIZONTAL_CENTER = stick_config["left"]["horizontal-center"]
L_VERTICAL_CENTER = stick_config["left"]["vertical-center"]
R_DEADZONE = stick_config["right"]["deadzone"]
R_HORIZONTAL_CENTER = stick_config["right"]["horizontal-center"]
R_VERTICAL_CENTER = stick_config["right"]["vertical-center"]

SCALE = stick_config["scale"]


def deadzone(value, deadzone_value):
    if value > deadzone_value:
        return value - deadzone_value
    elif value < -deadzone_value:
        return value + deadzone_value
    else:
        return 0


def normalise_stick(stick, side):
    if side == "left":
        deadzone_value = L_DEADZONE
        horizontal_center = L_HORIZONTAL_CENTER
        vertical_center = L_VERTICAL_CENTER
    elif side == "right":
        deadzone_value = R_DEADZONE
        horizontal_center = R_HORIZONTAL_CENTER
        vertical_center = R_VERTICAL_CENTER
    else:
        raise ValueError("Invalid side")

    x = stick[0]
    y = stick[1]
    return (
        deadzone((x - horizontal_center) / SCALE, deadzone_value),
        -deadzone((y - vertical_center) / SCALE, deadzone_value),
    )


def load_config(path):
    with open(path) as f:
        config = yaml.load(f, Loader=SafeLoader)
        return config
