#!/usr/bin/env python3
# Requires PyAudio and PySpeech.
 
import speech_recognition as sr
from time import ctime
import time
import os
from gtts import gTTS
import random
from pygame import mixer

r = sr.Recognizer()
##A phrase used to awaken Oswald
awaken = ["Oswald awaken"]
awake = False

mixer.init()

##Opening phrases
welcome_phrases = ['What can I do for you?', 'What\'s up Alex?', 'How can I be of assistance?']

greeting = random.randint(0, len(welcome_phrases)-1)
 
def speak(audioString):
    print(audioString)
    tts = gTTS(text=audioString, lang='en')
    tts.save("audio.mp3")
    os.system("mpg321 audio.mp3")
    mixer.music.load('audio.mp3')
    mixer.music.play()
 
def recordAudio():
    # Record Audio
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)
 
    # Speech recognition using Google Speech Recognition
    data = ""
    try:
        # Uses the default API key
        # To use another API key: `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
        data = r.recognize_google(audio)
        print("You said: " + data)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
 
    return data

while 1:
    data = recordAudio()
    jarvis(data)
