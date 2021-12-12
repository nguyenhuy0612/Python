
import speech_recognition as sr
from gtts import gTTS
from playsound import playsound
from datetime import datetime

mic = sr.Recognizer()

#!---------------------------------------------------
with sr.Microphone() as source:
    playsound('./Eshop.wav')
    audio = mic.record(source,duration=5)
    playsound('./Eshop.wav')
#!---------------------------------------------------

#?---------------------------------------------------
    try:
        text = mic.recognize_google(audio, language='th')
    except:
        text = 'Excuse me'

    print(text)

    #google = gTTS(text, lang="th")
    #google.save("./Seech.mp3")
    #playsound('./Seech.mp3')
#?---------------------------------------------------