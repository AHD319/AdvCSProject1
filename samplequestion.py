from gpiozero import Button
from RPLCD.i2c import CharLCD
import time


lcd = CharLCD('PCF8574', 0x27)
#width and length of lcd display
width = 16
length = 2

# define buttons
button1 = Button(19, pull_up=True)
button2 = Button(6, pull_up=True)
button3 = Button(17, pull_up=True)
button4 = Button(22, pull_up=True)
# question and multiple choice answers. the space at the begining to give time for user to read

question = "     print('Hello World') prints..."
options = ["     1. hello", "2. hello world", "3. Hello World", "4. world"]
#turning array into string by seperating each element with "|"
options_string = " | ".join(options)
# indentitfy correct button (corresponding to answer)
correct_button = button3

# manual scroll because question is long, the number of loops is the number of characters being shifted. Its calauclated by subtratcing number of letters in question by the width of the lcd and adding 1 because im using slice function that removes last letter
for i in range(len(question)-width+1):
    # adding position of where text starts (not neccessary because already default)
    lcd.cursor_pos = (0,0)
    # this shifts the string each loop, when i is 0 it would go from 0:16 filiing the row ("     print("hel") each time i increases, the whole string shifts and the question reveals, the i+width gives the end of the string
    lcd.write_string(question[i:i+width])
    time.sleep(0.5)
    # delay transition for thinking
time.sleep(3)
lcd.clear()
for i in range(len(options_string)-width+1):
    # goes one row down to display options
    lcd.cursor_pos = (1,0)
    lcd.write_string(options_string[i:i+width])
    time.sleep(.5)
    
# function for correct answer when button 3 is pressed
def correct():
    lcd.clear()
    lcd.write_string("correct")
# function for incorrect answer when any wrong button is pressed
def incorrect():
    lcd.clear()
    lcd.write_string("incorrect")
# when any button other than 3 is pressed lcd prints incorrect.
button1.when_pressed = incorrect
button2.when_pressed = incorrect
button3.when_pressed = correct
button4.when_pressed = incorrect


