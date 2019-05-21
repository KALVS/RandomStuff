import urllib.request
with urllib.request.urlopen('http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=12345') as response:
   html = str(response.read())

print(html)

import re
number  = re.findall('nothing=(.*)', html)
