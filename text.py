# text.py

import pyttsx3


class Speaker:
    def __init__(self, language="en"):
        self.engine = pyttsx3.init()
        voices = self.engine.getProperty("voices")

        for voice in voices:
            if "naayf" in voice.name.lower() or "hoda" in voice.name.lower() or "arabic" in voice.name.lower():
                self.engine.setProperty("voice", voice.id)
              
                break
    

    def say(self, text):
        self.engine.say(text)
        self.engine.runAndWait()