import os
from PIL import Image
import io
import base64
import random

def get_alphabet_images(phrase, alphabet_directory):
    images = []
    for char in phrase:
        char = char.lower()
        if char.isalpha():
            char_dir = os.path.join(alphabet_directory, char)
            if os.path.exists(char_dir) and os.path.isdir(char_dir):
                # Get a random image from the alphabet sub-directory
                image_files = [f for f in os.listdir(char_dir) if f.endswith(('png', 'jpg', 'jpeg'))]
                if image_files:
                    image_path = os.path.join(char_dir, random.choice(image_files))
                    with Image.open(image_path) as img:
                        buffered = io.BytesIO()
                        img.save(buffered, format="PNG")
                        img_str = base64.b64encode(buffered.getvalue()).decode()
                        images.append(f"data:image/png;base64,{img_str}")
    return images

def handle_phrase(phrase, video_directory, alphabet_directory):
    phrase_dir = os.path.join(video_directory, phrase)
    if os.path.exists(phrase_dir) and os.path.isdir(phrase_dir):
        video_files = [f for f in os.listdir(phrase_dir) if f.endswith(('mp4', 'avi', 'mov'))]
        if video_files:
            return {"type": "video", "data": os.path.join(phrase, random.choice(video_files))}

    images = get_alphabet_images(phrase, alphabet_directory)
    if images:
        return {"type": "images", "data": images}

    return {"type": "error", "message": "No video or images found for the given phrase"}
