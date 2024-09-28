import pyaudio
import wave
from pydub import AudioSegment
from datetime import datetime

def record_audio(output_filename, duration=5, channels=2, rate=44100, chunk=1024):
    audio = pyaudio.PyAudio()

    stream = audio.open(format=pyaudio.paInt16,
                        channels=channels,
                        rate=rate,
                        input=True,
                        frames_per_buffer=chunk)

    frames = []

    print("Recording...")

    for i in range(0, int(rate / chunk * duration)):
        data = stream.read(chunk)
        frames.append(data)

    print("Finished recording.")

    stream.stop_stream()
    stream.close()
    audio.terminate()

    with wave.open(output_filename, 'wb') as wf:
        wf.setnchannels(channels)
        wf.setsampwidth(audio.get_sample_size(pyaudio.paInt16))
        wf.setframerate(rate)
        wf.writeframes(b''.join(frames))

def convert_to_mp3(input_filename, output_filename):
    sound = AudioSegment.from_wav(input_filename)
    sound.export(output_filename, format="mp3")

def start_record_and_save():
    filename = str(datetime.now())
    output_filename = f"./outputs/audio/{filename}.wav"
    mp3_output_filename = f"./outputs/audio/{filename}.mp3"
    duration = 5  

    record_audio(output_filename, duration=duration)
    convert_to_mp3(output_filename, mp3_output_filename)

    print(f"Audio recorded and saved as {mp3_output_filename}")
    
    return filename
