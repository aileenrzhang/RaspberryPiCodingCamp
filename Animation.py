from picamera import PiCamera
from time import sleep
from gpiozero import Button

button = Button(17)
camera = PiCamera()
 
camera.start_preview()
frame = 1 #If you have stopped your code and want to continue, make this number the next frame number!!
#If you leave it as 1, you will overwrite your own work!!


while True:
    try:
        button.wait_for_press()
        camera.capture('/home/pi/Desktop/Coding_Camp/frame%03d.jpg' % frame)
        frame += 1
    except KeyboardInterrupt:
        camera.stop_preview()
        break