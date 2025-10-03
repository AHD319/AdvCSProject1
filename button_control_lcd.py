from gpiozero import Button
from RPLCD.i2c import CharLCD


# Setup LCD (I2C address usually 0x27, 16x2 L# Setup button (GPIO17)
lcd = Charlcd('PCF8574', 0x27)

# defining 2 buttons and their gpio pins
button = Button(19, pull_up=True)
button2 = Button(22, pull_up=True)


# displays hello world on lcd when program starts
lcd.clear()
lcd.write_string("Hello World!")

# function to clear lcd 
def clear_text():
    lcd.clear()
    
#function to print welcome on lcd
def show_welcome():
    lcd.clear()
    lcd.write_string("Welcome")

# applying functions to buttons, when button2 is pressed it clears lcd and when button is pressed it prints welcome
button2.when_pressed = clear_text
button.when_pressed = show_welcome

