import pyttsx3
import pythoncom
import datetime

engine = pyttsx3.init('sapi5')
voice = engine.getProperty('voices')
# print(voice[1].id)
engine.setProperty('voice',voice[1].id)

def Speak(text):
    engine.say(text)
    engine.runAndWait()

# Speak('Good evening ! My name is dishant.')

def greet():
    h = datetime.datetime.now().hour
    # if h > 0 and h < 12:
    #     Speak('Good morning!')
    if 0 < h < 12:
        Speak('Good morning!')
    elif 12 < h < 18:
        Speak('Good afternoon')
    elif 18 < h < 20:
        Speak('Good evening')
    else:
        Speak('Good night')

greet()