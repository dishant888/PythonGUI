from win32com.client import Dispatch

def Say(text):
    Dispatch('SAPI.SpVoice').Speak(text)