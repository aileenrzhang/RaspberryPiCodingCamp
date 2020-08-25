from picamera import PiCamera
from time import sleep

camera = PiCamera()
 
camera.start_preview()
frame = 1


while frame < 600:
    sleep(6)
    camera.capture('/home/pi/Desktop/Timelapse/frame%03d.jpg' % frame)
    frame += 1
    
camera.stop_preview()