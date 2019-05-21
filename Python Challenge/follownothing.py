import urllib3
import re


def following(url):

    print(url)
    req = http.request('GET', url)
    link = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing='
    number  = re.findall('nothing is ([0-9]*)', str(req.data))
    link += number[0]
    
    return (link)

http = urllib3.PoolManager()
#r = http.request('GET', 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=12345')
#Fullnumber = str(r.data)
#number  = re.findall('nothing is ([0-9]*)', Fullnumber)
link = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=8022'



for i in range(0,400):
    link = following(link)

