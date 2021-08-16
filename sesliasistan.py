import speech_recognition as sr
from datetime import datetime
import webbrowser
import time
from gtts import gTTS
from playsound import playsound
import random
import os


r =sr.Recognizer()

def record(ask = False):
    with sr.Microphone()as source:
        if ask:
            speak(ask)
        audio = r.listen(source)
        voice =''
        try:
            voice = r.recognize_google(audio,language ='tr-TR')
        except sr.UnknownValueError:
            speak('anlayamadım')
        return voice

    
def cevap(voice):
    if 'pazartesi hangi dersler var' in voice:
        speak("matematik ")
    if 'video aç' in voice:
        searchb = record('ne aramak istiyorsunuz ?')
        urlb = 'https://www.youtube.com/results?search_query='+ searchb
        webbrowser.get().open(urlb)
        speak(searchb + 'için bulduklarım')
    if 'dünyadaki en iyi anne kim 'in voice:
        speak("dilek başaran")
    if 'nasılsın'in voice:
        speak("iyi senden")
    if 'dünyadaki en iyi anne nerede'in voice:
        speak("türkiye istanbul ümraniye namık kemal mahallesi gezi sokak bahar apartmanı no altı")
    if 'saat kaç' in voice:
        speak(datetime.now().strftime('%H:%M:%S'))
    if 'arama yap' in voice:
        search = record('ne aramak istiyorsunuz ?')
        url = 'https://www.google.com/search?q='+ search
        webbrowser.get().open(url)
        speak(search + 'için bulduklarım')
    if 'uygulamadan çık' in voice:
        speak("görüşürüz")
        exit()
    
def speak(string):
    tts = gTTS(string,lang ='tr')
    rand =random.randint(1,100000)
    file = 'audio-'+str(rand)+'.mp3'
    tts.save(file)
    playsound(file)
    os.remove(file)
    

    
  
    
    
    
speak("nasıl yardımcı olabilirim")
time.sleep(1)
while 1:
     voice =record()
     print(voice)
     cevap(voice)
    
