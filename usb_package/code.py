import time
import board
import neopixel
import digitalio
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.keycode import Keycode

# Define some Variables to use later
keyboard = Keyboard(usb_hid.devices)
layout = KeyboardLayoutUS(keyboard)
buttons = {}
button_map = (
    #Name of Button, Pin on Board, Action to take, Value of that action
    ('UpLeft',board.GP28,'function','button_action_1'),
    ('UpRight',board.GP6,'keypress',Keycode.END),
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
def button_action_1():
    print("I'll perform special Action !")
    pixels.brightness = 0.5
    pixels.fill((255, 0, 0))
    # Example 1 : Writing Some text :
    layout.write("Never Gona Give you up!\n")
    time.sleep(0.5)
    layout.write("RickRoll!!!!!")
    time.sleep(0.5)
    # Example 2 : Pressing Keys 
    keyboard.press(Keycode.SHIFT, Keycode.X)
    keyboard.release_all

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
    pixels.fill((0, 255, 0))
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

