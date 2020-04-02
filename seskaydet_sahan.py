from playsound import playsound
from gtts import gTTS
import speech_recognition as sr
import os
def SesKaydedici(metin,seskaynak):
    new_metin = gTTS(text=metin, lang='tr')
    new_metin.save("Audio/"+seskaynak)
