from picamera import PiCamera
from time import sleep
from gpiozero import Button

button = Button(17)
camera = PiCamera()
 

frame = 1 #If you have stopped your code and want to continue, make this number the next frame number!!
#If you leave it as 1, you will overwrite your own work!!


while True:
    try:
        button.wait_for_press()
        camera.start_preview()
        camera.preview.alpha = 128
        sleep(3)
        camera.capture('/home/pi/Animation/frame%03d.jpg' % frame)
        camera.stop_preview()
        frame += 1
    except KeyboardInterrupt:
        break