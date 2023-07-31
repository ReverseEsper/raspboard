import time
import board
import neopixel
import digitalio
import usb_hid
from adafruit_hid.mouse import Mouse
import microcontroller

# Define some Variables to use later
mouse = Mouse(usb_hid.devices)

startup = microcontroller.nvm[0]

pixels = neopixel.NeoPixel(board.GP16, 1)
pixels.brightness = 0.01

if startup == 2:
    pixels.fill(255,0,0)
else:
    pixels.fill(0,255,0)

time.sleep(3)

#while True:
for _ in range(100)
    pixels.fill((0,0,255))
    for i in range (10):
        mouse.move(10,0,0)
        time.sleep(0.1)
    for i in range (10):
        mouse.move(0,10,0)
        time.sleep(0.1)
    for i in range (10):
        mouse.move(-10,0,0)
        time.sleep(0.1)
    for i in range (10):
        mouse.move(0,-10,0)
        time.sleep(0.1)
    # Repeat next loop 10ms later
    time.sleep(0.01)

