import time
from smbus2 import SMBus
import speech_recognition as sr
from collections import deque

CAP1203_ADDR = 0x28
MAIN_CONTROL = 0x00
SENSOR_INPUT_STATUS = 0x03
LED_LINKING = 0x72
PRODUCT_ID = 0xFD
MANUFACTURER_ID = 0xFE
REVISION = 0xFF

r = sr.Recognizer()
bus = SMBus(1)

# Keep track of last few touches for swipe detection
touch_history = deque(maxlen=5)

def cap1203_init():
    product_id = bus.read_byte_data(CAP1203_ADDR, PRODUCT_ID)
    manufacturer_id = bus.read_byte_data(CAP1203_ADDR, MANUFACTURER_ID)
    revision = bus.read_byte_data(CAP1203_ADDR, REVISION)
    print(f"CAP1203 Found -> Product ID: {product_id}, Manufacturer: {manufacturer_id}, Revision: {revision}")
    bus.write_byte_data(CAP1203_ADDR, MAIN_CONTROL, 0x00)
    bus.write_byte_data(CAP1203_ADDR, LED_LINKING, 0x00)

def read_touch():
    touch_status = bus.read_byte_data(CAP1203_ADDR, SENSOR_INPUT_STATUS)

    touch_data = {
        "CH1": bool(touch_status & 0x01),
        "CH2": bool(touch_status & 0x02),
        "CH3": bool(touch_status & 0x04),
    }

    # Log only active touches
    for ch, state in touch_data.items():
        if state:
            if not touch_history or touch_history[-1] != ch:  # avoid duplicates
                touch_history.append(ch)

    return touch_data

def detect_swipe():
    # Convert history to string for easier checking
    seq = "".join(touch_history)

    if "CH1CH2CH3" in seq:
        return "RIGHT"
    elif "CH3CH2CH1" in seq:
        return "LEFT"
    return None

def start_speech_recognition():
    with sr.Microphone() as source:
        print("Listening...")
        audio_text = r.listen(source, timeout=5, phrase_time_limit=5)
        print("Processing...")

        try:
            text = r.recognize_google(audio_text)
            print("You said:", text)
        except Exception as e:
            print(f"Speech recognition error: {e}")

if __name__ == "__main__":
    cap1203_init()
    try:
        while True:
            touches = read_touch()
            swipe = detect_swipe()
            if swipe:
                print(f"Swipe detected: {swipe}, starting speech recognition...")
                start_speech_recognition()
                touch_history.clear()  # reset after action

            time.sleep(0.1)

    except KeyboardInterrupt:
        bus.close()
