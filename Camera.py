from picamera import PiCamera
from time import sleep

camera = PiCamera()
 
camera.start_preview()
sleep(5)
camera.capture('/home/pi/Desktop/Coding_Camp/frame01.jpg')
camera.stop_preview()
