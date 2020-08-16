from time import sleep
from gpiozero import Button

button = Button(17)

while (True):
    camera.start_preview()
    button.wait_for_press()
    camera.capture('/home/pi/image.jpg')
    camera.stop_preview()