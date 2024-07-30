import time

import whisper


class Transcriber:
    def __init__(self, model_name="base", device="cuda"):
        self.model = whisper.load_model(model_name, device=device)

    def transcribe(self, audio_path, progress_callback):
        audio = whisper.load_audio(audio_path)
        audio = whisper.pad_or_trim(audio)
        mel = whisper.log_mel_spectrogram(audio).to(self.model.device)
        _, probs = self.model.detect_language(mel)
        language = max(probs, key=probs.get)

        for i in range(1, 101):
            time.sleep(0.05)
            progress_callback(i)

        options = whisper.DecodingOptions()
        result = whisper.decode(self.model, mel, options)
        return language, result.text
