# PKG

This Python package provides a simple interface for text-to-speech conversion using a multilingual TTS model, allowing users to generate speech from text with customizable voice characteristics.

## Description:

This Python package offers an easy-to-use wrapper around the TTS library for text-to-speech conversion. Key features include:
- Multilingual Support: Utilizes the "tts_models/multilingual/multi-dataset/xtts_v2" model, enabling speech synthesis in multiple languages.
- Voice Customization: Allows users to provide a speaker WAV file to customize the voice characteristics of the generated speech.
- Language Selection: Supports specifying the target language for accurate pronunciation and intonation.
- File Output: Generates audio files directly from text input, saving the result to a specified output path.
- Progress Tracking: Includes a progress bar for monitoring the speech generation process.
- Simple API: Offers a straightforward function call to generate speech from text, making it accessible for developers of various skill levels.

This package is ideal for developers and researchers working on applications that require high-quality, multilingual speech synthesis, such as accessibility tools, language learning software, or voice-enabled interfaces.

## How to install:

Run the following command in your python venv:

```sh
pip install git+https://github.com/avivilloz/tts.git@main#egg=tts
```

Or add the following line to your project's `requirement.txt` file:

```
git+https://github.com/avivilloz/tts.git@main#egg=tts
```

And run the following command:

```sh
pip install -r requirements.txt
```

## How to use:

```python
from tts import generate_text_to_speech

# Example usage
text_to_speak = "Hello, this is a test of the text-to-speech system."
output_file = "output_speech.wav"
speaker_sample = "path/to/speaker_sample.wav"

generate_text_to_speech(
    text=text_to_speak,
    output_path=output_file,
    speaker_wav_path=speaker_sample,
    language="en"
)

print(f"Speech generated and saved to {output_file}")
```