from time import sleep
from gpiozero import Button

button = Button(17)

while (True):
    button.wait_for_press()
    print("Hello")
    sleep(1)