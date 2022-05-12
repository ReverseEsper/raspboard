import time
import board
import digitalio
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.keycode import Keycode
from adafruit_hid.mouse import Mouse
import microcontroller

# Piny
# 29 : lewy górny
# 4  : prawy górny
# 8,10,12,14 - strzałki

time.sleep(3)




keyboard = Keyboard(usb_hid.devices)
keyboard_layout = KeyboardLayoutUS(keyboard)

btn_a = digitalio.DigitalInOut(board.GP8)
btn_a.direction = digitalio.Direction.INPUT
btn_a.pull = digitalio.Pull.DOWN

btn_b = digitalio.DigitalInOut(board.GP10)
btn_b.direction = digitalio.Direction.INPUT
btn_b.pull = digitalio.Pull.DOWN

btn_c = digitalio.DigitalInOut(board.GP12)
btn_c.direction = digitalio.Direction.INPUT
btn_c.pull = digitalio.Pull.DOWN

btn_d = digitalio.DigitalInOut(board.GP14)
btn_d.direction = digitalio.Direction.INPUT
btn_d.pull = digitalio.Pull.DOWN

btn_lg = digitalio.DigitalInOut(board.GP28)
btn_lg.direction = digitalio.Direction.INPUT
btn_lg.pull = digitalio.Pull.DOWN

btn_pg = digitalio.DigitalInOut(board.GP6)
btn_pg.direction = digitalio.Direction.INPUT
btn_pg.pull = digitalio.Pull.DOWN

layout = KeyboardLayoutUS(keyboard)

bs_p = False

while True:

    if btn_d.value:
        keyboard.press(Keycode.LEFT_ARROW)
    else:
        keyboard.release(Keycode.LEFT_ARROW)

    if btn_c.value:
        keyboard.press(Keycode.UP_ARROW)
    else:
        keyboard.release(Keycode.UP_ARROW)

    if btn_b.value:
        keyboard.press(Keycode.DOWN_ARROW)
    else:
        keyboard.release(Keycode.DOWN_ARROW)

    if btn_a.value:
        keyboard.press(Keycode.RIGHT_ARROW)
    else:
        keyboard.release(Keycode.RIGHT_ARROW)

    if btn_lg.value:
        keyboard.press(Keycode.HOME)
    else:
        keyboard.release(Keycode.HOME)

    if btn_pg.value:
        keyboard.press(Keycode.END)
    else:
        keyboard.release(Keycode.END)
	
    time.sleep(0.01)

