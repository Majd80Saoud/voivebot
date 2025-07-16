# VoiveBot AI

Welcome to VoiceBot AI, an interactive English-speaking assistant powered by Whisper and Cohere.  
This bot listens to your voice, understands your question, generates an intelligent response, and speaks it back — all within seconds!

## What Can It Do?

✅ Convert your voice to text using Whisper (offline, accurate)  
✅ Generate smart, natural responses using Cohere's Chat API  
✅ Speak replies out loud using pyttsx3 (Text-to-Speech)  
✅ Fully works with English voice & text

---

## Tech Stack

| Feature              | Library / API            |
|----------------------|--------------------------|
| Speech-to-Text       | faster-whisper         |
| Response Generation  | cohere (Chat API)      |
| Text-to-Speech (TTS) | pyttsx3 (offline)      |
| Audio Recording      | sounddevice, scipy   |

---

## 📁 Project Structure
│
├── main.py        # Main logic: listen → respond → speak
├── voice.py       # Handles audio recording & transcription
├── text.py        # Handles voice output (TTS)
