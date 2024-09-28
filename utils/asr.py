from faster_whisper import WhisperModel

def transcribe_audio(filename):
    model_size = "large-v3"

    model = WhisperModel(model_size, device="cpu", compute_type="int8")

    # to use gpu
    # model = WhisperModel(model_size, device="cuda", compute_type="float32")

    segments, info = model.transcribe(f"./outputs/audio/{filename}.mp3", beam_size=5)

    final_text = ""

    for segment in segments:
        final_text += segment.text
    
    with open(f"./outputs/text/{filename}.txt", "w") as file:
        file.write(final_text)


