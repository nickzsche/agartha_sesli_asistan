from playsound import playsound
from gtts import gTTS
import speech_recognition as sr
import os

def SesCal(cal):
    playsound("Audio/"+cal)