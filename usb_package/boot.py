import storage, usb_cdc
import board, digitalio

# On the Circuit Playground, pressing an on-board button
# connects the button to +V.

button = digitalio.DigitalInOut(board.GP28)
button.direction = digitalio.Direction.INPUT
button.pull = digitalio.Pull.DOWN

# Disable devices only if button is not pressed.
if not button.value:
	#storage.disable_usb_drive()
	#usb_cdc.disable()
    print("This would turn off the device")