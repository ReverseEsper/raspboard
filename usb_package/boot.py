import storage
import board, digitalio


button = digitalio.DigitalInOut(board.GP28)
button.direction = digitalio.Direction.INPUT
button.pull = digitalio.Pull.DOWN

# If you reset with that button pressed USB drive will show up. Otherwise it won't
if not button.value:
	storage.disable_usb_drive()
