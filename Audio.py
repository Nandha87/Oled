import speech_recognition as sr

# Create a recognizer
r = sr.Recognizer()

# List all available microphones
print("Available microphones:")
for i, mic in enumerate(sr.Microphone.list_microphone_names()):
    print(i, mic)

# Use the Google VoiceHAT mic (change the index if needed)
mic_index = None
for i, mic in enumerate(sr.Microphone.list_microphone_names()):
    if "voiceHAT" in mic or "Google" in mic:
        mic_index = i
        break

if mic_index is None:
    print("❌ Google voiceHAT mic not found!")
else:
    print(f"✅ Using mic index {mic_index}")
    with sr.Microphone(device_index=mic_index) as source:
        print("Say something...")
        r.adjust_for_ambient_noise(source)  # Helps reduce noise
        audio = r.listen(source)

    try:
        text = r.recognize_google(audio)
        print("You said:", text)
    except sr.UnknownValueError:
        print("Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))
