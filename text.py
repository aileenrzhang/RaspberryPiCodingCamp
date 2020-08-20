from picamera import PiCamera, Color
from time import sleep

camera = PiCamera()

camera.start_preview()
camera.annotate_background = Color('blue')
camera.annotate_foreground = Color('yellow')
camera.annotate_text_size = 75
camera.annotate_text = " Hello world "
sleep(5)
camera.capture('/home/pi/Desktop/Coding_Camp/text_image.jpg')
camera.stop_preview()