import time
import board
import digitalio
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode

# Sleep so HID has time to set up keyboard
time.sleep(3)

button_map = (
    #Name of Button, Pin on Board, Action to take, Value of that action
    ('UpLeft',board.GP28,'keypress',Keycode.HOME),
    ('UpRight',board.GP6,'keypress',Keycode.END),
    ('Left',board.GP14,'keypress',Keycode.LEFT_ARROW),
    ('Right',board.GP8,'keypress',Keycode.RIGHT_ARROW),
    ('Up',board.GP12,'keypress',Keycode.UP_ARROW),
    ('Down',board.GP10,'keypress',Keycode.DOWN_ARROW)    
)

# Init Buttons
buttons = {}
for button in button_map:
    b_name = button[0]
    b_pin = button[1]
    buttons[b_name]= digitalio.DigitalInOut(b_pin)
    buttons[b_name].direction = digitalio.Direction.INPUT
    buttons[b_name].pull = digitalio.Pull.DOWN

# Loop for checking for buttons
keyboard = Keyboard(usb_hid.devices)
while True:
    for button in button_map:
        b_name = button[0]
        b_action = button[2]
        b_value = button[3]
        if b_action == 'keypress':
            if buttons[b_name].value:
                keyboard.press(b_value)
            else:
                keyboard.release(b_value)
	
    time.sleep(0.01)

