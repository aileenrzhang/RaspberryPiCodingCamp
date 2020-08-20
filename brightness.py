from picamera import PiCamera
from time import sleep

camera = PiCamera()
 
camera.start_preview()
frame = 64

camera.start_preview()
for i in range(100):
    camera.annotate_text = "Brightness: %s" % i
    camera.brightness = i
    camera.capture('/home/pi/Desktop/Coding_Camp/frame%03d.jpg' % frame)
    sleep(0.1)
    frame+=1
camera.stop_preview()
