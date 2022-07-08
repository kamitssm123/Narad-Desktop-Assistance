import assistance_details
from speak import speak
from database import speech_mode

def output(o):
    if speech_mode():
        speak(o)
        print(assistance_details.name + " : " + o)
        print()

    else:
        print(assistance_details.name + " : " + o)
        print() 