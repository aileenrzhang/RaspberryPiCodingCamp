from picamera import PiCamera
from time import sleep
from gpiozero import Button

button = Button(17)
camera = PiCamera()
 
camera.start_preview()
frame = 64

camera.start_preview()
for mode in camera.EXPOSURE_MODES:
    camera.exposure_mode = mode
    camera.annotate_text = "Effect: %s" % mode
    camera.capture('/home/pi/Desktop/Coding_Camp/frame%03d.jpg' % frame)
    sleep(5)
    frame+=1
camera.stop_preview()