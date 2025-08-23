import time
from smbus2 import SMBus
import speech_recognition as sr

# CAP1203 I2C address and registers
CAP1203_ADDR = 0x28
MAIN_CONTROL = 0x00
SENSOR_INPUT_STATUS = 0x03
LED_LINKING = 0x72
PRODUCT_ID = 0xFD
MANUFACTURER_ID = 0xFE
REVISION = 0xFF

r = sr.Recognizer()
bus = SMBus(1)


def cap1203_init():
    try:
        product_id = bus.read_byte_data(CAP1203_ADDR, PRODUCT_ID)
        manufacturer_id = bus.read_byte_data(CAP1203_ADDR, MANUFACTURER_ID)
        revision = bus.read_byte_data(CAP1203_ADDR, REVISION)

        print(
            f"CAP1203 Found -> Product ID: {product_id}, "
            f"Manufacturer: {manufacturer_id}, Revision: {revision}"
        )

        # Reset control and disable LED linking
        bus.write_byte_data(CAP1203_ADDR, MAIN_CONTROL, 0x00)
        bus.write_byte_data(CAP1203_ADDR, LED_LINKING, 0x00)
    except Exception as e:
        print(f"Error initializing CAP1203: {e}")


def read_touch():
    try:
        touch_status = bus.read_byte_data(CAP1203_ADDR, SENSOR_INPUT_STATUS)

        if bool(touch_status & 0x01):  # Channel 1 touch
            try:
                with sr.Microphone() as source:
                    print("Channel 1 touched → Speak now...")
                    audio_text = r.listen(source, timeout=5, phrase_time_limit=5)
                    print("Processing speech...")

                    # Try Google recognition
                    try:
                        print("You said: " + r.recognize_google(audio_text))
                    except Exception as e:
                        print(f"Speech recognition error: {e}")
            except Exception as e:
                print(f"Microphone error: {e}")

        return {
            "CH1": bool(touch_status & 0x01),
            "CH2": bool(touch_status & 0x02),
            "CH3": bool(touch_status & 0x04),
        }
    except Exception as e:
        print(f"Error reading CAP1203: {e}")
        return {"CH1": False, "CH2": False, "CH3": False}


if __name__ == "__main__":
    cap1203_init()
    try:
        while True:
            touches = read_touch()
            print(touches)
            time.sleep(0.2)
    except KeyboardInterrupt:
        print("\nExiting...")
        bus.close()
