from gtts import gTTS
from playsound import playsound


def speak(text):
    tts = gTTS(text,lang='en', tld='co.in')
    tts.save('text.mp3')
    playsound('text.mp3')

