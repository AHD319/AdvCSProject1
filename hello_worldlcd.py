# importing charlcd from rplcd for the i2c lcd
from RPLCD.i2c import CharLCD
#importing time for delay
import time

#identitfy lcd address (0x27)
lcd = CharLCD('PCF8574', 0x27)
#when starting lcd it first has to clear
lcd.clear()
#function to display text
lcd.write_string("Hello, World!")
#displays text for 3 seconds
time.sleep(3)
#clears display
lcd.clear()