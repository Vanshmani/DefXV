import json
import base64
import io
from PIL import Image
import matplotlib.pyplot as plt

IMAGE_DISPLAY_DURATION = 1  # seconds

def decode_base64_to_image(base64_str):
    image_data = base64.b64decode(base64_str)
    image = Image.open(io.BytesIO(image_data))
    print("Image decode completed")
    return image

def display_image(letter, images_dict):
    if letter in images_dict:
        image = decode_base64_to_image(images_dict[letter])
        if image is None:
            print(f"Could not decode the image for letter {letter}")
            return
        else:
            plt.imshow(image)
            plt.axis('off')  # Hide axes
            plt.title(f"Image for {letter}")
            plt.show(block=False)
            plt.pause(IMAGE_DISPLAY_DURATION)
            plt.close()
    else:
        print(f"No image found for letter {letter}")

def handle_file(filename, images_dict):
    with open(filename, 'r') as file:
        for line in file:
            line = line.strip()
            print(f"Read from file: {line}")

            for letter in line:
                if letter != ' ':
                    display_image(letter.upper(), images_dict)

def load_images_from_json():
    json_filename = "./utils/asl_signs.json"
    with open(json_filename, 'r') as json_file:
        images_dict = json.load(json_file)
        print("JSON file loaded")
    return images_dict