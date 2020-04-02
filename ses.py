#metni sese dönüştürmek için
from playsound import playsound
from gtts import gTTS
import speech_recognition as sr
#sistem dosyalarını daha rahat şekilde açmak için
import os
ad= input("Merhaba Adınız Nedir? ")
#Burada kullanacağımız 2 parametre bulunuyor, Dil ve Text
sarki = """Daracık daracık sokaklar
Kızlar misket yuvarlar
Kızlara koca vermiyor
Kocaman kocaman hanımlar"""
tts = gTTS(text=sarki, lang='tr')
tts2 = gTTS(text="Merhaba "+ad +" sana nasıl yardımcı olabilirim?", lang='tr')
#Burada oluşturduğumuz ses dosyasını konuma merhaba.mp3 diye kaydediyoruz
tts2.save("Audio/ad.mp3")
#şimdi ise bu dosyayı açalım.
playsound('Audio/ad.mp3')

y1 = input(" Yaz ")
dene =y1.upper()
dene2 = dene.split()
liste = ["ŞARKI","ŞİİR","OYUN"]
for i in dene2:
    if i in liste[0]:
        playsound("merhaba.mp3")
    if i in liste[1]:
        print("Şiir Bilmiyorum Şimdilik...")
