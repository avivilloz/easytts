from TTS.api import TTS


tts = TTS(
    model_name="tts_models/multilingual/multi-dataset/xtts_v2",
    progress_bar=True,
)


def generate_text_to_speech(
    text: str, output_path: str, speaker_wav_path: str, language: str = "en"
):
    tts.tts_to_file(
        text=text,
        file_path=output_path,
        speaker_wav=speaker_wav_path,
        language=language,
    )
