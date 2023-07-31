import storage
import board, digitalio
import microcontroller

button = digitalio.DigitalInOut(board.GP28)
button.direction = digitalio.Direction.INPUT
button.pull = digitalio.Pull.DOWN

# To access USB disk, press Left Upper button during bootup.
if not button.value:
	microcontroller.nvm[0]=1
	#storage.disable_usb_drive()
else:
	microcontroller.nvm[0]=2
