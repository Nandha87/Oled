import RPi.GPIO as GPIO
from luma.core.interface.serial import spi
from luma.oled.device import ssd1306
from luma.core.render import canvas
from PIL import ImageFont
import time

# Disable GPIO warnings
GPIO.setwarnings(False)

# SPI connection (CE0 = GPIO 8)
serial = spi(device=0, port=0, gpio_DC=24, gpio_RST=25)
device = ssd1306(serial, rotate=0)

# Load default font
font = ImageFont.load_default()

try:
    # Draw a test screen
    with canvas(device) as draw:
        draw.rectangle(device.bounding_box, outline="white", fill="black")
        draw.text((10, 10), "Hello Pi Zero 2W!", font=font, fill="white")
        draw.text((10, 30), "SSD1306 SPI Test", font=font, fill="white")

    # Keep display on for 10 seconds
    time.sleep(2000)

finally:
    # Cleanup GPIO on exit
    GPIO.cleanup
