import json 
from pprint import pprint

with open('Abbott701_Veronika555_74.json') as x:
	data = json.load(x)

rtypes = []

for x in data['entry']:
	y = x['resource']['resourceType']
	rtypes.append(y)

rtypes = list(set(rtypes))
rtypes.sort()
print(rtypes)
#CarePlan
uI = []
for x in data['entry']:
	u = []
	y = x['resource']['resourceType']
	if y == "CarePlan":
		for count in range(len(x['resource']['category'][0]['coding'])):
			u.append(x['resource']['category'][0]['coding'][count]['display'])
		u.append(x['resource']['status'])
		for z in x['resource']['activity']:
			u.append(z['detail']['code']['coding'][0]['display'])
		uI.append(u)

#Condition
cI = []
for x in data['entry']:
	c = []
	y = x['resource']['resourceType']
	if y == "Condition":
		c.append(x['resource']['code']['coding'][0]['display'])
		c.append(x['resource']['clinicalStatus'])
		c.append(x['resource']['verificationStatus'])
		c.append(x['resource']['assertedDate'])
		cI.append(c)

#DiagnosticReport
dI = []
for x in data['entry']:
	d = []
	y = x['resource']['resourceType']
	if y == "DiagnosticReport":
		d.append(x['resource']['status'])
		d.append(x['resource']['code']['coding'][0]['display'])
		d.append(x['resource']['effectiveDateTime'])
		d.append(x['resource']['issued'])
		dI.append(d)

#Claim
clI = []
for x in data['entry']:
	cl = []
	y = x['resource']['resourceType']
	if y == "Claim":
		cl.append(x['resource']['status'])
		cl.append(x['resource']['use'])
		cl.append(x['resource']['billablePeriod'])
		for z in x['resource']['item']:
			cl.append((z['net']['value'], z['net']['code']))
			try:
				cl.append(x['resource']['encounter']['status'])
				cl.append(x['resource']['encounter']['class']['code'])
			except KeyError:
				cl.append(None)
				cl.append(None)

			try:
				x['resource']['reason'][0]['coding'][0]['display']
			except KeyError:
				cl.append(None)
		cl.append((x['resource']['total']['value'], x['resource']['total']['code']))
		clI.append(cl)

print(clI)