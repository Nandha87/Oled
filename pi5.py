from luma.core.interface.serial import spi
from luma.lcd.device import st7565
from luma.core.render import canvas
from PIL import ImageFont

# SPI connection
serial = spi(port=0, device=0, gpio_DC=24, gpio_RST=25)

# Create device object (128x64 LCD)
device = st7565(serial, width=128, height=64)

# Draw something
with canvas(device) as draw:
    draw.rectangle(device.bounding_box, outline="white", fill="black")
    draw.text((20, 20), "Hello Pi5!", fill="white")
