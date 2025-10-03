from gpiozero import Button
from RPLCD.i2c import CharLCD
import time

lcd = CharLCD('PCF8574', 0x27)
width = 16

button1 = Button(19, pull_up=True)
button2 = Button(6, pull_up=True)
button3 = Button(17, pull_up=True)
button4 = Button(22, pull_up=True)
# function to continouly detect a button being pressed, once its pressed its stored into the pressed variable and can be used in if statments
def wait_for_button():
    while True:
        if button1.is_pressed:
            return button1
        if button2.is_pressed:
            return button2
        if button3.is_pressed:
            return button3
        if button4.is_pressed:
            return button4
        time.sleep(0.05)

question1 = "     print('Hello World') prints..."
options1 = ["1. hello", "2. hello world", "3. Hello World", "4. world"]

question2 = "     Where did name Java come from?"
options2 = ["1. Minecraft", "2. Java Coffee", "3. Javascript", "4. none"]

def Q1():
    lcd.clear()
    for i in range(len(question1) - width + 1):
        lcd.cursor_pos = (0, 0)
        lcd.write_string(question1[i:i + width])
        time.sleep(0.3)
    time.sleep(1)
    lcd.clear()
    options_string = " | ".join(options1)
    for i in range(len(options_string) - width + 1):
        lcd.cursor_pos = (1, 0)
        lcd.write_string(options_string[i:i + width])
        time.sleep(0.3)
        # checking what button has been pressed from the wait for button function
    pressed = wait_for_button()
    lcd.clear()
    if pressed == button3:
        lcd.write_string("correct")
    else:
        lcd.write_string("incorrect")
    time.sleep(3)
    #moving on to next question after 3 seconds
    Q2()

def Q2():
    lcd.clear()
    for i in range(len(question2) - width + 1):
        lcd.cursor_pos = (0, 0)
        lcd.write_string(question2[i:i + width])
        time.sleep(0.3)
    time.sleep(1)
    lcd.clear()
    options_string = " | ".join(options2)
    for i in range(len(options_string) - width + 1):
        lcd.cursor_pos = (1, 0)
        lcd.write_string(options_string[i:i + width])
        time.sleep(0.3)
    pressed = wait_for_button()
    lcd.clear()
    if pressed == button2:
        lcd.write_string("correct")
    else:
        lcd.write_string("incorrect")

lcd.clear()
lcd.write_string("welcome to Quiz")
lcd.cursor_pos = (1, 0)
lcd.write_string("Press any Button")

wait_for_button()
Q1()
