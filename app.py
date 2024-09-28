import sounddevice as sd
import vosk
import json
import sys
import threading
import queue
import os

model_path1 = os.path.join(os.getcwd(),'models','VOSK-SMALL-INDIAN-ENGLISH-0.4')

model = vosk.Model(model_path1)
recognizer = vosk.KaldiRecognizer(model, 16000)

buffered_text = ""
audio_queue = queue.Queue()

def callback(indata, frames, time, status):
    if status:
        print(status, file=sys.stderr)
    audio_queue.put(bytes(indata))

def recognition_thread():
    global buffered_text
    while True:
        audio_data = audio_queue.get()
        if recognizer.AcceptWaveform(audio_data):
            result = recognizer.Result()
            result_dict = json.loads(result)
            text = result_dict.get("text", "")
            if text:
                words = text.split()
                for word in words:
                    print(word)
                buffered_text = "" 
        else:
            partial_result = recognizer.PartialResult()
            result_dict = json.loads(partial_result)
            partial_text = result_dict.get("partial", "")
            buffered_text += partial_text

recognition_thread = threading.Thread(target=recognition_thread, daemon=True)
recognition_thread.start()

with sd.RawInputStream(samplerate=16000, blocksize=4096, dtype='int16', channels=1, callback=callback):
    print("Listening...")
    try:
        while True:
            sd.sleep(1000)
    except KeyboardInterrupt:
        print("Stopped listening")