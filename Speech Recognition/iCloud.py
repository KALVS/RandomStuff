
from pyicloud import PyiCloudService
from datetime import date
from re import findall


iCloudService = PyiCloudService('alextraino@icloud.com', 'Br3sbane.')
from_dt = date(2018, 6, 19)
to_dt = date(2018, 6, 19)
iCalEvents = iCloudService.calendar.events(from_dt, to_dt)

#iCalEvents_title = findall("'title': '.*'", iCalEvents)

iCalEvent = str(iCalEvents[0])

iCaltitle = findall("'title': '([ A-Za-z]*)'", iCalEvent)
print(iCaltitle)
