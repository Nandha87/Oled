from luma.core.interface.serial import spi
from luma.oled.device import ssd1306
from luma.core.render import canvas
from PIL import ImageFont

# SPI: port=0, device=0 → CE0 is used
# gpio_DC = GPIO 24, gpio_RST = GPIO 25
serial = spi(device=0, port=0, gpio_DC=24, gpio_RST=25)
device = ssd1306(serial, rotate=0)

# Optional: load a default font
font = ImageFont.load_default()

# Draw something
with canvas(device) as draw:
    draw.rectangle(device.bounding_box, outline="white", fill="black")
    draw.text((10, 10), "Hello Pi Zero 2W!", font=font, fill="white")
    draw.text((10, 30), "SSD1306 SPI Test", font=font, fill="white")
