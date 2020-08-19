from picamera import PiCamera
from time import sleep
from gpiozero import Button

button = Button(17)
camera = PiCamera()
 
camera.start_preview()
frame = 42

camera.start_preview()
for effect in camera.IMAGE_EFFECTS:
    camera.image_effect = effect
    camera.annotate_text = "Effect: %s" % effect
    camera.capture('/home/pi/Desktop/Coding_Camp/frame%03d.jpg' % frame)
    sleep(5)
    frame+=1
camera.stop_preview()