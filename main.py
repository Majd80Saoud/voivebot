import cohere
from voice import Recognizer
from text import Speaker


COHERE_API_KEY =''


co = cohere.Client(COHERE_API_KEY)


stt = Recognizer(language="en")
text_input = stt.listen()
print(f"📝 You said: {text_input}")


response = co.chat(
    message=text_input,
    model="command-r",
    chat_history=[
        {"role": "system", "message": "Always reply in English only."}
    ]
)
reply = response.text.strip()
print(f"🤖 Response: {reply}")

# 3. تحويل الرد إلى صوت (بالإنجليزية)
tts = Speaker(language="en")
tts.say(reply)