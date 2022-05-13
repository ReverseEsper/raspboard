import storage
import board, digitalio


button = digitalio.DigitalInOut(board.GP28)
button.direction = digitalio.Direction.INPUT
button.pull = digitalio.Pull.DOWN

# To access USB disk, press Left Upper button during bootup.
if not button.value:
	storage.disable_usb_drive()
