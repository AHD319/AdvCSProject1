# libraries for button function
from gpiozero import Button
import time
#define button
button = Button(19, pull_up=True)
#forever loop
while True:
    # to check that button is being pressed it prints pressed or not pressed
    if button.is_pressed:
        print("Pressed")
    else:
        print("Not pressed")
    time.sleep(0.5)