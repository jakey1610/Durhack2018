import json 
from pprint import pprint

with open('/Users/Sami/Desktop/DurHack/test.json') as x:
	data = json.load(x)

rtypes = []

for x in data['entry']:
	y = x['resource']['resourceType']
	rtypes.append(y)

rtypes = list(set(rtypes))
print(rtypes)