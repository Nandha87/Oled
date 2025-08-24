import speech_recognition as sr

def main():
    r = sr.Recognizer()

    # List microphones
    print("Available microphones:")
    for i, mic_name in enumerate(sr.Microphone.list_microphone_names()):
        print(f"[{i}] {mic_name}")

    # ---- Select your mic ----
    # Change this index to match the USB mic shown above
    mic_index = 1  

    with sr.Microphone(device_index=mic_index, sample_rate=48000, chunk_size=2048) as source:
        print(f"\nUsing microphone: {sr.Microphone.list_microphone_names()[mic_index]}")
        print("Calibrating for ambient noise (2s)... please stay quiet")
        r.adjust_for_ambient_noise(source, duration=2)

        print("Listening... (say something within 20s)")
        try:
            audio = r.listen(source, timeout=20, phrase_time_limit=20)
            print("✅ Audio captured!")

            # Optional: try to recognize
            try:
                text = r.recognize_google(audio)
                print("You said:", text)
            except sr.UnknownValueError:
                print("❌ Could not understand the audio")
            except sr.RequestError as e:
                print("⚠️ Could not request results; check internet connection:", e)

        except sr.WaitTimeoutError:
            print("❌ Timeout: no speech detected")

if __name__ == "__main__":
    main()
