from gpiozero import Button
from RPLCD.i2c import CharLCD
import time

lcd = CharLCD('PCF8574', 0x27)
width = 16

button1 = Button(19, pull_up=True)
button2 = Button(6, pull_up=True)
button3 = Button(17, pull_up=True)
button4 = Button(22, pull_up=True)
# added a score to add on for each correct answer and show at the results view at the end
score = 0
# function to continouly detect a button being pressed when its called, once its pressed its stored into the pressed variasble and can be used in if statments. Instead of waiting for a button press at any time, it calls it a at a specfic time which is after the options are displayed.
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
# all questions and options, the option_string was removed because I didnt need one for each question, instead I could just change its value each question.

question1 = "Q1:     print('Hello World') prints..."
options1 = ["   1. hello", "2. hello world", "3. Hello World", "4. world"]

question2 = "Q2:     Where did name Java come from?"
options2 = ["   1. Minecraft", "2. Java Coffee", "3. Javascript", "4. none"]

question3 = "Q3:     Which of these is a list in python?"
options3 = ["   1. {1,2,3}", "2. (1,2,3)", "3. 1,2,3", "4, [1,2,3]"]

question4 = "Q4:     indentation does not matter in python..."
options4 = ["   1/2. (True)", "3/4. (False)"]

question5 = "Q5:     what is 10 % 3 ?"
options5 = ["   1. (1) ", "2. (3.33)", "3, (0)", "4, (10)"]

def Q1():
    # functions dont recognize score as a global variable so this is needed
    global score
    lcd.clear()
    # length of the question minus the width of the lcd (because text is already there) + 1 because slice function removes last letter
    for i in range(len(question1) - width + 1):
        lcd.cursor_pos = (0, 0)
        # prints the question from 0:16 (i:i+width) and each time i increases the text shifts and reveals the whole question (2:18, 5:23)
        lcd.write_string(question1[i:i + width])
        time.sleep(0.3)
    time.sleep(1)
    lcd.clear()
    options_string = " | ".join(options1)
    for i in range(len(options_string) - width + 1):
        lcd.cursor_pos = (1, 0)
        lcd.write_string(options_string[i:i + width])
        time.sleep(0.3)
        # this calls the function wait for button, from now on it detects any button press and uses it as the pressed variable in the if statments below, after a button is pressed it no longer detects until called again
    pressed = wait_for_button()
    lcd.clear()
    if pressed == button3:
        lcd.write_string("correct")
        #adding 1 score if the answer was correct
        score += 1
    else:
        lcd.write_string("incorrect")
        # after it says correct or incorrect it waits 3 seconds then moves on to next question.
    time.sleep(3)
    Q2()

def Q2():
    global score
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
        score += 1
    else:
        lcd.write_string("incorrect")
    time.sleep(3)
    Q3()

def Q3():
    global score
    lcd.clear()
    for i in range(len(question3) - width + 1):
        lcd.cursor_pos = (0, 0)
        lcd.write_string(question3[i:i + width])
        time.sleep(0.3)
    time.sleep(1)
    lcd.clear()
    options_string = " | ".join(options3)
    for i in range(len(options_string) - width + 1):
        lcd.cursor_pos = (1, 0)
        lcd.write_string(options_string[i:i + width])
        time.sleep(0.3)
    pressed = wait_for_button()
    lcd.clear()
    if pressed == button4:
        lcd.write_string("correct")
        score += 1
    else:
        lcd.write_string("incorrect")
    time.sleep(3)
    Q4()
def Q4():
    global score
    lcd.clear()
    for i in range(len(question4) - width + 1):
        lcd.cursor_pos = (0, 0)
        lcd.write_string(question4[i:i + width])
        time.sleep(0.3)
    time.sleep(1)
    lcd.clear()
    options_string = " | ".join(options4)
    for i in range(len(options_string) - width + 1):
        lcd.cursor_pos = (1, 0)
        lcd.write_string(options_string[i:i + width])
        time.sleep(0.3)
    pressed = wait_for_button()
    lcd.clear()
    # this is a true or false question so i made it so that if buttons 3 or 4 are pressed then its false and if buttons 1 or 2 are pressed then its true making it 50%
    if pressed == button3 or pressed == button4:
        lcd.write_string("correct")
        score += 1
    else:
        lcd.write_string("incorrect")
    time.sleep(3)
    Q5()

def Q5():
    global score
    lcd.clear()
    for i in range(len(question5) - width + 1):
        lcd.cursor_pos = (0, 0)
        lcd.write_string(question5[i:i + width])
        time.sleep(0.3)
    time.sleep(1)
    lcd.clear()
    options_string = " | ".join(options5)
    for i in range(len(options_string) - width + 1):
        lcd.cursor_pos = (1, 0)
        lcd.write_string(options_string[i:i + width])
        time.sleep(0.3)
    pressed = wait_for_button()
    lcd.clear()
    if pressed == button1:
        lcd.write_string("correct")
        score += 1
    else:
        lcd.write_string("incorrect")
    time.sleep(3)
    results()
        
def results():
    global score
    lcd.clear()
    # if the score is more than or equal to 3, lcd prints congrats and prints score under, if the score is equal to or less than 2, it prints, you can do better and the score under
    if score >= 3:
        lcd.write_string("Congrats :)")
        lcd.cursor_pos = (1, 0)
        #adding score variable in string
        lcd.write_string(f"You Scored {score}/5")
    elif score <= 2:
        lcd.write_string("You can do better :(")
        lcd.cursor_pos = (1, 0)
        lcd.write_string(f"You Scored {score}/5")
lcd.clear()
lcd.write_string("welcome to Quiz")
lcd.cursor_pos = (1, 0)
lcd.write_string("Press any Button")

wait_for_button()
Q1()
