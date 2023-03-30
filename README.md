# Joycon for desktop

Allows you to use your Nintendo Switch Joycons as a keyboard and mouse.
The keybinds and hotkeys can be changed in the `config.yaml` file.

## Install

1. You should have [Python][install-python] and [Make][install-make] installed. [You are could use this program without make](#run-without-make), but using make will make it a lot easier.
2. Open a terminal in this directory
3. *Optional* Create a virtual environment
   - run `python -m venv venv` to create a virtual environment
   - On MacOS or Linux: run `./venv/Scripts/activate` to activate it
   - On Windows: run `.\venv\Scripts\activate` to activate it.
4. Run `make update` to install the required packages

To run the program, activate the virtual environment (if you made one), and run `make run` in the terminal.
Make sure you have the Joycons connected to your computer before running.

[install-python]: <https://realpython.com/installing-python/#how-to-install-python-on-windows>
[install-make]: <https://tilburgsciencehub.com/building-blocks/configure-your-computer/automation-and-workflows/make/>

## How to use

The keybinds are set in the `config.yaml` file.
For an example configuration, `config.default.yaml` and the sections below.
Other settings can be changes in the `settings.yaml` file.
To change apply the changes, restart the program.

### Setting up the analog sticks

The analog sticks are used to move the mouse, and scroll the mouse wheel.

```YaML
left:
  analog-stick:
    wheel:
      scroll_direction: vertical
      scroll_speed: 0.8

  ... rest of the buttons ...

right:
  analog-stick:
    mouse:
      mouse_speed: 2.0
```

The block above is the default configuration. It sets the left analog stick to scroll the mouse wheel, and the right analog stick to move the mouse.
The `scroll_speed` and `mouse_speed` can be changed to your preference. The `scroll_direction` can be set to `vertical` or `horizontal`.
To switch the modes of the analog sticks place the `mouse` or `wheel` block under the `left` or `right` block.

### Setting up the buttons

The buttons are used to press keys on the keyboard.

```YaML
left:
  buttons:
    down: down
    up: up
    right: right
    left: left
    left_sr: a
    left_sl: b
    l: _
    zl: ctrl+c
    minus: _
    stick_l_btn: _
    capture: toggle-motion
```

The block above shows a configuration for the left controller. The d-pad is set to the arrow keys, and the `sr` and `sl` buttons are set to `a` and `b` respectively.
It is also possible to set multiple keys to a button. For example, the `zl` button is set to `ctrl+c`, which means that when the `zl` button is pressed, the `ctrl` and `c` keys are pressed at the same time.
To unbind a button, set it to `_`.
The modifier keys can be set with the following values: `alt`, `ctrl`, `shift`, `windows`
To use mouse buttons, use the following values: `mouse-left`, `mouse-middle`, `mouse-right`
To toggle motion controls, use the value `toggle-motion`.

### Using motion controls

Motion controls can be used to move the mouse by pointing at your screen.

```YaML
motion:
  side: right
  sensitivity: 1.0
  smoothing: 0.25
  min-distance: 8
```

The block above shows the default configuration. The `side` can be set to `left` or `right`. The `sensitivity` can be changed to your preference.
The `smoothing` is the amount of smoothing applied to the mouse movement. Smoothing can be used to reduce the jitter of the mouse, but it will also make the mouse movements less responsive.
The `min-distance` is the minimum distance(in pixels) the Joycon has to move before the mouse starts moving. This is useful te prevent drag-clicking when you are not moving the Joycon. Setting this value to high will make the mouse feel jumpy, but setting it to low will make it harder to click things without dragging.

To enable motion controls bind a button to the `toggle-motion` value. Place the Joycon on a flat surface(or hold it still for a moment) pointing to the middle of the screen. Then press the button you bound to `toggle-motion`.
The Joycon will now take a second to calibrate, and after that it will start moving the mouse, towards the middle of the screen. Now you can move the Joycon to move the mouse.
To disable motion controls, press the button you bound to `toggle-motion` again.

> make sure you change your screen resolution to the resolution of your screen in the `settings.yaml` file.

### Changing application settings

The application settings can be found in the `settings.yaml` file.

```YaML
app:
  refresh-speed: 0.01
  path-config: config.yaml
  screen:
    width: 1920
    height: 1080
```

The block above shows the default settings. The `refresh-speed` is the time between each cycle of the program. Turing this value up will slow the program down. This is useful when the mouse movements are too fast.
The `path-config` is the path to the `config.yaml` file. You can make multiple configurations, and change this path to the one you want to use.
The `screen` block is used to set the resolution of your screen. This is used to calculate the mouse movement when using motion controls. Make sure you set this to the resolution of your screen.

### Calibrating the Joycons

Im going to admit, the calibration is a bit of a mess, but it is usable.
To calibrate the Joycons, run `make calibrate` in the terminal.
The terminal will now print all the values of the analog sticks like this:

```text
left: {'horizontal': 1963, 'vertical': 2284}, right: {'horizontal': 2169, 'vertical': 1784}
```

The calibration can be found in the `settings.yaml` file.

```YaML
joystick:
  scale: 300.0
  left:
    deadzone: 1.0
    horizontal-center: 1963
    vertical-center: 2284
```

The block above shows the configuration for the left analog stick. To change the configuration enter the values that were printed in the terminal to the corresponding fields.
The deadzone is the area around the center of the stick which is considered the middle. If the stick is in this area, the program will not register any movement. If you experience drift, increase the deadzone.
The scale is used to scale the movement of the analog stick. If you want to move the mouse, and scroll wheel faster, increase the scale, but i would recommend to leave it at 300.

## Run without Make

So you are to stubborn to download make? ...ok, i guess you can run the program without it. You just need to run the commands yourself. You can just use the instructions above, but replace Make commands with the following commands:

`make update` --> `python -m pip install --upgrade pip` and `pip install -r requirements.txt`

`make run` --> `python src/main.py`

`make calibrate` --> `python tools/calibrate.py`
