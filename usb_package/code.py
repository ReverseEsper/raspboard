import time
import board
import neopixel
import digitalio
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.keycode import Keycode
import microcontroller

# Define some Variables to use later
keyboard = Keyboard(usb_hid.devices)
layout = KeyboardLayoutUS(keyboard)
buttons = {}
startup = microcontroller.nvm[0]
if startup == 2:
        button_map = (
        # If You started Board with Upper Left button pressed, aside from enabling Drive, that button will now perform different funcion
        ('UpLeft',board.GP28,'function','show_github_on_windows'),
        ('UpRight',board.GP6,'keypress',Keycode.PAGE_DOWN),
        ('Left',board.GP14,'keypress',Keycode.LEFT_ARROW),
        ('Right',board.GP8,'keypress',Keycode.RIGHT_ARROW),
        ('Up',board.GP12,'keypress',Keycode.UP_ARROW),
        ('Down',board.GP10,'keypress',Keycode.DOWN_ARROW)
    )
else:
    button_map = (
        # Name of Button, Pin on Board, Action to take, Value of that action
        # Button codes are here : https://docs.circuitpython.org/projects/hid/en/latest/api.html#adafruit-hid-keycode-keycode
        ('UpLeft',board.GP28,'keypress',Keycode.PAGE_UP),
        ('UpRight',board.GP6,'keypress',Keycode.PAGE_DOWN),
        ('Left',board.GP14,'keypress',Keycode.LEFT_ARROW),
        ('Right',board.GP8,'keypress',Keycode.RIGHT_ARROW),
        ('Up',board.GP12,'keypress',Keycode.UP_ARROW),
        ('Down',board.GP10,'keypress',Keycode.DOWN_ARROW)
    )




# Sleep so HID has time to set up keyboard
time.sleep(3)

# Board RP2040 Zero constains RGB led called NeoPixel.
# It actually is microcontroller on itself and you can control it
pixels = neopixel.NeoPixel(board.GP16, 1)
pixels.brightness = 0.01

# Example Function that shows how to use buttons features
# First it show how to use function layout.write , type some text as keyboard
# Then it show how to press specific keys on keyboard
# Map Example : ('UpLeft',board.GP28,'function','button_action_1'),
def show_github_on_windows():
    pixels.brightness = 0.5
    # Green Color
    pixels.fill((255, 0, 0))
    keyboard.send(Keycode.CONTROL,Keycode.ESCAPE)
    time.sleep(1)
    layout.write("https://github.com/ReverseEsper/raspboard\n")
    time.sleep(0.5)
    # Example 2 : Pressing Keys
    pixels.brightness = 0.01


# Init Buttons
for button in button_map:
    b_name = button[0]
    b_pin = button[1]
    buttons[b_name]= digitalio.DigitalInOut(b_pin)
    buttons[b_name].direction = digitalio.Direction.INPUT
    buttons[b_name].pull = digitalio.Pull.DOWN

# Loop for checking for buttons
while True:
    pixels.fill((0,255,0))
    for button in button_map:
        b_name = button[0]
        b_action = button[2]
        b_value = button[3]
        if b_action == 'keypress':
            if buttons[b_name].value:
                keyboard.press(b_value)
            else:
                keyboard.release(b_value)
        elif b_action == 'function':
            if buttons[b_name].value:
                eval(b_value+'()')

	
    # Repeat next loop 10ms later
    time.sleep(0.01)

