import whisper

#model = whisper.load_model("base")
model = whisper.load_model("base", device="cuda")

# load audio and pad/trim it to fit 30 seconds
#audio = whisper.load_audio("TestFiles/WhatsApp Ptt 2024-07-17 at 14.24.29.mp3")
audio = whisper.load_audio("TestFiles/TM7.m4a")
audio = whisper.pad_or_trim(audio)

# make log-Mel spectrogram and move to the same device as the model
mel = whisper.log_mel_spectrogram(audio).to(model.device)

# detect the spoken language
_, probs = model.detect_language(mel)
print(f"Detected language: {max(probs, key=probs.get)}")

# decode the audio
options = whisper.DecodingOptions()
result = whisper.decode(model, mel, options)

# print the recognized text
print(result.text)
