from flask import Flask, jsonify, render_template, send_from_directory
from speech_to_text import recognize_speech_from_microphone
from phrase_handler import handle_phrase

app = Flask(__name__)
video_directory = "Data-Set/Videos"  # Replace with the path to your video directory
alphabet_directory = "Data-Set/Alphabet"  # Replace with the path to your alphabet directory


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/process', methods=['POST'])
def process():
    phrase = recognize_speech_from_microphone()
    if phrase.startswith("Could not"):
        return jsonify({"error": phrase})

    result = handle_phrase(phrase, video_directory, alphabet_directory)
    result["recognized_phrase"] = phrase  # Add recognized phrase to the result
    return jsonify(result)


@app.route('/video/<path:filename>')
def video(filename):
    return send_from_directory(video_directory, filename)


if __name__ == "__main__":
    app.run(debug=True)
