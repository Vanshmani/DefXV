import speech_recognition as sr

def recognize_speech_from_microphone():
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()

    with microphone as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source, duration=1)  # Adjust for ambient noise
        audio = recognizer.listen(source)

    try:
        phrase = recognizer.recognize_google(audio)
        print(f"Recognized phrase: {phrase}")
        return phrase
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
        return "Could not request results from Google Speech Recognition service"
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand the audio")
        return "Could not understand the audio"

if __name__ == "__main__":
    recognize_speech_from_microphone()
