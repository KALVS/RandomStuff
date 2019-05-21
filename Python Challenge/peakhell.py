import pickle, io, urllib3, pprint
from pickle import Unpickler

http = urllib3.PoolManager()
text = http.request('GET', 'http://www.pythonchallenge.com/pc/def/banner.p')
tempstr = text.data
unpickld = pickle.loads(tempstr)

for row in unpickld:
   print(''.join(pair[0] * pair[1] for pair in row))
   
pprint.pprint(a)    
