from speech_to_text import SpeechToText
from phrase_handler import PhraseHandler

def main():
    videos_directory = "Data-Set/Videos"
    alphabet_directory = "Data-Set/Alphabet"

    stt = SpeechToText()
    handler = PhraseHandler(videos_directory, alphabet_directory)

    while True:
        print("Say something:")
        audio_data = stt.listen()
        phrase = stt.recognize_speech(audio_data)

        if phrase:
            handler.search_and_play(phrase)
            handler.clear_cache()
        else:
            print("Sorry, I couldn't understand. Please try again.")

if __name__ == "__main__":
    main()
