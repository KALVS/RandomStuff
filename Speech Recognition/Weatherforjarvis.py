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

town = input('What town are you in?\n')

weather = 'http://api.openweathermap.org/data/2.5/weather?q='+town+',AU&appid=eccbc53293f9233984b66fc892ee71fe'

weather_data = urlopen(weather).read()
weather_data = str(weather_data)

minimal_temp = findall('"temp_min":(.*),"temp_max"', weather_data)
minimal_temp = float(minimal_temp[0])

maximum_temp = findall('"temp_max":(.*)},"vis', weather_data)
maximum_temp = float(maximum_temp[0])

minimal_temp = minimal_temp - 273.15

maximum_temp = maximum_temp - 273.15

avg_temp = (minimal_temp + maximum_temp) / 2

print('average temp = ' + str(avg_temp))
print ('maximum temp = ' + str(maximum_temp))
print ('minimum temp = ' + str(minimal_temp))
