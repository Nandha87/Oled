import uc1701x
import RPi.GPIO as GPIO
from time import sleep

# Pin mapping for Raspberry Pi 5
DC  = 24   # GPIO24
RST = 25   # GPIO25
CS  = 8    # GPIO8 (CE0)

# Initialize LCD
lcd = uc1701x.LCD(dc=DC, rst=RST, cs=CS, spi_bus=0, spi_dev=0)

# Clear screen
lcd.clear()

# Write some text
lcd.text("Hello Pi5!", 0, 0)     # (text, x, y)
lcd.text("LCD Test OK", 0, 16)
lcd.display()

# Hold message for 5 seconds
sleep(5)

# Clear again
lcd.clear()
lcd.display()
