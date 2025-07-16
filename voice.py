# voice.py

import sounddevice as sd
import numpy as np
import tempfile
import scipy.io.wavfile
from faster_whisper import WhisperModel

class Recognizer:
    def __init__(self, language="en"):
        self.language = language
        self.model = WhisperModel("base", compute_type="int8")  

    def listen(self, duration=5, samplerate=16000):
        print("🎤 Listening...")

        recording = sd.rec(int(duration * samplerate), samplerate=samplerate, channels=1, dtype='int16')
        sd.wait()

        with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as f:
            scipy.io.wavfile.write(f.name, samplerate, recording)
            segments, _ = self.model.transcribe(f.name, language=self.language)

            text = ""
            for segment in segments:
                text += segment.text
            return text.strip()