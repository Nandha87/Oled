from luma.core.interface.serial import i2c
from luma.oled.device import ssd1306
from PIL import Image, ImageDraw, ImageFont


serial = i2c(port=1, address=0x3C)  # 0x3C is common address
device = ssd1306(serial)


device.clear()


image = Image.new("1", (device.width, device.height), "black")
draw = ImageDraw.Draw(image)

font = ImageFont.load_default()

draw.text((10, 20), "Hello Pi 5!", font=font, fill="white")


device.display(image)
