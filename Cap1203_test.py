import time
from smbus2 import SMBus

# CAP1203 I2C address and registers
CAP1203_ADDR = 0x28
MAIN_CONTROL = 0x00
SENSOR_INPUT_STATUS = 0x03
PRODUCT_ID = 0xFD
MANUFACTURER_ID = 0xFE
REVISION = 0xFF

bus = SMBus(1)

def cap1203_init():
    # Read chip IDs
    product_id = bus.read_byte_data(CAP1203_ADDR, PRODUCT_ID)
    manufacturer_id = bus.read_byte_data(CAP1203_ADDR, MANUFACTURER_ID)
    revision = bus.read_byte_data(CAP1203_ADDR, REVISION)

    print(f"CAP1203 detected -> Product ID: {product_id}, Manufacturer: {manufacturer_id}, Revision: {revision}")

    # Reset MAIN_CONTROL
    bus.write_byte_data(CAP1203_ADDR, MAIN_CONTROL, 0x00)


def read_touch():
    touch_status = bus.read_byte_data(CAP1203_ADDR, SENSOR_INPUT_STATUS)
    return {
        "CH1": bool(touch_status & 0x01),
        "CH2": bool(touch_status & 0x02),
        "CH3": bool(touch_status & 0x04),
    }


if __name__ == "__main__":
    cap1203_init()
    try:
        while True:
            touches = read_touch()
            print(touches)   # Print touch states
            time.sleep(0.2)
    except KeyboardInterrupt:
        print("\nExiting...")
        bus.close()
