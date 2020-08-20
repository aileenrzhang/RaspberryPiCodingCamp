from picamera import PiCamera
from time import sleep

camera = PiCamera()
 
camera.start_preview()
frame =1

camera.start_preview()
for i in range(100):
    camera.annotate_text = "Contrast: %s" % i
    camera.contrast = i
    camera.capture('/home/pi/Desktop/Coding_Camp/Contrast/frame%03d.jpg' % frame)
    sleep(0.1)
    frame+=1
camera.stop_preview()

