from luma.core.interface.serial import spi
from luma.oled.device import ssd1306
from luma.core.render import canvas
from luma.core.interface.serial import noop
from luma.core.virtual import viewport
from luma.core.interface import gpio

# Use periphery GPIO instead of RPi.GPIO
gpio = gpio.get_gpio('periphery')

# SPI0 CE0 = /dev/spidev0.0
serial = spi(port=0, device=0, gpio_DC=24, gpio_RST=None, gpio=gpio)

device = ssd1306(serial)

with canvas(device) as draw:
    draw.text((10, 20), "Hello Pi5!", fill="white")

print("✅ Sent test text to OLED on Pi5")
