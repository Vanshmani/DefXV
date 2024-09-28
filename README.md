# DefXV - AI-Powered AR Glasses for the Deaf and Mute Community

## Overview
DefXV is an AI/ML-integrated Augmented Reality (AR) glass solution designed to bridge the communication gap for the deaf and mute community. This cutting-edge project leverages advanced machine learning models and augmented reality technology to facilitate seamless two-way communication between individuals who rely on sign language and those who do not. The system offers real-time Voice-to-Sign and Sign-to-Voice translations, making it easier for people to understand each other.

### Key Features
- **Voice-to-Sign Conversion:** Translates spoken words into sign language animations with 97% accuracy.
- **Sign-to-Voice Translation:** Captures sign language gestures and converts them into voice with 95% precision.
- **3D Avatar Integration:** Displays sign language using 3D avatars, offering an interactive and intuitive communication experience.
- **Design Patent:** The DefXV project has earned a design patent, showcasing its innovative approach to assistive technology.

---

## Architecture and Technology Stack

### 1. Data Collection & Preprocessing
The system was trained using a vast dataset of sign language gestures, voice samples, and corresponding text. The data was preprocessed to ensure high-quality input for training:
- **Image Data:** Used OpenCV for capturing sign language gestures from videos.
- **Audio Data:** Preprocessed using the Librosa library to extract features from spoken language.
- **Text Data:** Tokenized and preprocessed using NLTK to improve the accuracy of text-based translation.

### 2. AI/ML Models

#### A. Voice-to-Sign Conversion
- **Model Used:** Transformer-based Speech Recognition Model (e.g., DeepSpeech or Wav2Vec2)
- **Process:** Converts audio inputs into text, which is then translated into sign language using a pre-trained Transformer model.
- **Training:** Utilized supervised learning with a large dataset of paired speech and sign language text to achieve high accuracy.

#### B. Sign-to-Voice Translation
- **Model Used:** Convolutional Neural Network (CNN) combined with Long Short-Term Memory (LSTM) layers for gesture recognition
- **Process:** Detects and interprets hand gestures using real-time video inputs, then translates them into corresponding speech using a text-to-speech model (e.g., Tacotron2).
- **Training:** The model was trained with video datasets of sign language gestures and labeled text, allowing it to learn gesture patterns effectively.

#### C. 3D Avatar Integration
- **Technology Used:** Unity with the XR Interaction Toolkit and Blender for creating and animating 3D avatars
- **Process:** The avatar system receives sign language translations from the ML model and animates the gestures in real-time, ensuring accurate and expressive sign representation.

### 3. AR Glasses Integration
- **Hardware:** Custom-designed AR glasses with built-in cameras, microphones, and speakers to facilitate real-time input and output.
- **Software:** Unreal Engine powers the AR experience, enabling users to view real-time sign language animations and voice translations through the glasses.

---

## System Workflow

1. **Voice-to-Sign Translation:**
   - The microphone captures spoken words.
   - The speech-to-text model processes the audio and converts it into text.
   - The text is then translated into sign language, displayed as 3D avatar animations on the AR glasses.

2. **Sign-to-Voice Translation:**
   - The camera captures the user's hand gestures.
   - The gesture recognition model identifies the signs and converts them into corresponding text.
   - A text-to-speech system vocalizes the translated text.

---

## Accuracy and Precision
- **Voice-to-Sign:** Achieves a 97% accuracy rate, ensuring minimal errors in capturing and translating spoken words.
- **Sign-to-Voice:** Offers 95% precision, providing reliable and consistent sign interpretation.

---

## Technologies & Tools Used
- **Programming Languages:** Python, C++
- **AI/ML Frameworks:** TensorFlow, PyTorch
- **NLP Libraries:** NLTK, Hugging Face Transformers
- **Audio Processing:** Librosa
- **Computer Vision:** OpenCV, MediaPipe
- **3D Animation:** Blender, Unity
- **AR Development:** Unreal Engine
- **Hardware Integration:** Arduino, Raspberry Pi

---

## Getting Started

### Prerequisites
- Python 3.8 or above
- PyTorch / TensorFlow
- OpenCV
- Unity 2020.3 or later
- Blender (for 3D modeling)
- Unreal Engine 5

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo/defxv.git
2. Install required Python packages:
   ```bash
   pip install -r requirements.txt
3. Set up the Unity and Unreal Engine projects following the documentation provided in the docs folder.

### Running the Project

1. For voice-to-sign translation
   ```bash
   python voice_to_sign.py

3. For sign-to-voice translation
   ```bash
   python sign_to_voice.py
   
## Challenges & Achievements
### Challenges
Building real-time translation with high accuracy was a significant challenge, especially in processing complex sign gestures and speech variations.

### Achievements
Developed a highly accurate and responsive system, secured a design patent, and achieved the goal of making communication accessible and effective for the deaf and mute community.

## Future Enhancements
### Language Expansion: 
Incorporate support for additional languages and regional sign variations.
### Emotion Recognition:
Implement AI models to detect and convey emotions during sign-to-voice translation.
### AR Glasses Optimization: 
Improve the hardware to ensure more seamless and comfortable long-term usage.

## Contact Information
For any inquiries, feel free to reach out:

##### Email: vanshmani389@gmail.com
##### LinkedIn: https://www.linkedin.com/in/founderspectov/


