from luma.core.interface.serial import spi
from luma.oled.device import ssd1306
from luma.core.render import canvas
from PIL import ImageFont

# Setup SPI connection
serial = spi(device=0, port=0, gpio_DC=23, gpio_RST=24)
device = ssd1306(serial)

# Draw something
with canvas(device) as draw:
    draw.text((10, 20), "Hello Pi5!", fill="white")

print("Message displayed on OLED")
