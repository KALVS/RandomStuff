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

iCloudService = PyiCloudService('alextraino@icloud.com', 'Br3sbane.')

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
