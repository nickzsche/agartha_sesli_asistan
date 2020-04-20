from sescalsahan import SesCal as sc
from seskaydet_sahan import SesKaydedici as sk
from ayir import HarfAyir as hf
from playsound import playsound
from gtts import gTTS
import speech_recognition as sr
import os

print("""ASİSTAN HENÜZ YAPIM AŞAMASINDA MODÜLLER SINIRLI""")

sc("ismin.mp3")
isim = input()
sk("Sana nasıl yardımcı olabilirim "+isim,"ad.mp3")
sc("ad.mp3")
sc("anlat.mp3")
ogren = input("")
dene =ogren.upper()
dene2 = dene.split()
liste = ["PYTHON","RUBY","JAVA"]
for i in dene2:
    if i in liste:
        sc("bilgi.mp3")
        if i == liste[0]:
            sc("python.mp3")
            sc("pythonnedir.mp3")
        if i == liste[1]:
            sc("ruby.mp3")
            sc("rubynedir.mp3")
        if i == liste == [2]:
            sc ("java.mp3")
        else:
            sc ("bilmiyorum.mp3")
