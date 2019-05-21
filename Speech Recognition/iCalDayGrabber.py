
from pyicloud import PyiCloudService
from datetime import date
from re import findall


iCloudService = PyiCloudService('alextraino@icloud.com', 'Br3sbane.')
from_dt = date.today()
to_dt = date.today()
iCalEvents = iCloudService.calendar.events(from_dt, to_dt)

iCalEvent = str(iCalEvents[0])
iCaltitle = findall("'title': '([ A-Za-z]*)'", iCalEvent)
print(iCalEvents)

