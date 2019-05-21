#!/usr/bin/env python3
# Requires PyAudio and PySpeech and more.

import speech_recognition as sr
from time import ctime
import time
import os
from gtts import gTTS
import random
from pygame import mixer
from pyicloud import PyiCloudService
from datetime import date
import re
from re import findall, finditer
from urllib.request import urlopen

#iCloud stuff. You gotta add you icloud login details here.
iCloudService = PyiCloudService('icloudemail.com', 'icloudPassword')
#Speech recognition recogniser used to call recognise audio google
r = sr.Recognizer()
##A phrase used to awaken Oswald
awaken = ["Jarvis"]
awake = False
#mixer is used to play the saved audio file which is Jarvis 'speaking'
mixer.init()

##Opening phrases
welcome_phrases = ['What can I do for you?', 'What\'s up?', 'How can I be of assistance?']

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

def awakenAlarm():
    # Record Audio
    with sr.Microphone() as source:
        audio = r.listen(source)

    # Speech recognition using Google Speech Recognition
    data = ""
    try:
        # Uses the default API key
        # To use another API key: `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
        speak('Processing')
        data = r.recognize_google(audio)
        print("You said: " + data)
        for i in range(0, len(awaken)):
            if awaken[i] in data:
                awake = True
                speak(welcome_phrases[greeting])
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

    return data

def jarvis(data):
    if "weather" in data:
        weather = 'http://api.openweathermap.org/data/2.5/weather?q=Brisbane,AU&appid=eccbc53293f9233984b66fc892ee71fe'
        weather_data = urlopen(weather).read()
        weather_data = str(weather_data)

        minimal_temp = findall('"temp_min":(.*),"temp_max"', weather_data)
        minimal_temp = float(minimal_temp[0])

        maximum_temp = findall('"temp_max":(.*)},"vis', weather_data)
        maximum_temp = float(maximum_temp[0])

        minimal_temp = minimal_temp - 273.15

        maximum_temp = maximum_temp - 273.15

        avg_temp = (minimal_temp + maximum_temp) / 2

        speak(str(avg_temp))

    if "events for today" in data:
        from_dt = date.today()
        to_dt = date.today()
        iCalEvents = iCloudService.calendar.events(from_dt, to_dt)

        iCalEvents = str(iCalEvents)
        iCalEvent_titles = findall("'title': '(.*)', 'location", iCalEvents)
        iCalEvent_location = findall("'location': (.*), 'startDate", iCalEvents)
        #iCalEvent = str(iCalEvents[0])
        #iCaltitle = findall("'title': '([ A-Za-z]*)'", iCalEvent)
        print(iCalEvents)
        for i in iCalEvent_titles:
            print(iCalEvent_titles)
            print(iCalEvent_location)

    if "how are you" in data:
        speak("I am fine")

    if "what time is it" in data:
        speak(ctime())

    if "where is" in data:
        data = data.split(" ")
        location = data[2]
        speak("Hold on Frank, I will show you where " + location + " is.")
        os.system("chromium-browser https://www.google.nl/maps/place/" + location + "/&amp;")

# initialization

#while(awake == False):
#    data = awakenAlarm()
while 1:
    data = recordAudio()
    jarvis(data)
