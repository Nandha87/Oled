from luma.core.interface.serial import spi
from luma.oled.device import ssd1306
from luma.core.render import canvas
from PIL import ImageFont

# SPI connection, DC on GPIO23
serial = spi(port=0, device=0, gpio_DC=23)

# Create display
device = ssd1306(serial)

# Draw test text
font = ImageFont.load_default()
with canvas(device) as draw:
    draw.text((10, 20), "Hello Pi5!", font=font, fill="white")

print("✅ Sent text to OLED")
