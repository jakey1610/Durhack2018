import json 
from pprint import pprint

# rtypes = []

# for x in data['entry']:
# 	y = x['resource']['resourceType']
# 	rtypes.append(y)

# rtypes = list(set(rtypes))
# rtypes.sort()

#CarePlan
def cPlan(file):
	data = json.load(open(file))
	uI = []
	for x in data['entry']:
		u = []
		y = x['resource']['resourceType']
		if y == "CarePlan":
			for count in range(len(x['resource']['category'][0]['coding'])):
				u.append(x['resource']['category'][0]['coding'][count]['display'])
			u.append(x['resource']['status'])
			u.append(x['resource']['activity'])
			u1 = {"condition": u[0], "status": u[1], "activities":u[2]}
			uI.append(u1)
	return uI



#Condition
def condition(file):
	data = json.load(open(file))
	cI = []
	for x in data['entry']:
		c = []
		y = x['resource']['resourceType']
		if y == "Condition":
			c.append(x['resource']['code']['coding'][0]['display'])
			c.append(x['resource']['clinicalStatus'])
			c.append(x['resource']['verificationStatus'])
			c.append(x['resource']['assertedDate'])
			c1 = {"condition": c[0], "clinicalStatus":c[1], "verificationStatus": c[2], "assertedDate": c[3]}

			cI.append(c1)
	return cI

#DiagnosticReport
def dReport(file):
	data = json.load(open(file))
	dI = []
	for x in data['entry']:
		d = []
		y = x['resource']['resourceType']
		if y == "DiagnosticReport":
			d.append(x['resource']['status'])
			d.append(x['resource']['code']['coding'][0]['display'])
			d.append(x['resource']['effectiveDateTime'])
			d.append(x['resource']['issued'])
			d1 = {"status": d[0], "document": d[1], "effectiveDateTime": d[2], "issued":d[3]}

			dI.append(d)
	return dI

# #Claim
# def claim(file):
# 	data = json.load(file)
# 	clI = []
# 	for x in data['entry']:
# 		cl = []
# 		y = x['resource']['resourceType']
# 		if y == "Claim":
# 			cl.append(x['resource']['status'])
# 			cl.append(x['resource']['use'])
# 			cl.append(x['resource']['billablePeriod'])
# 			cl1 = {"status": cl[0], "use": cl[1], "billablePeriod": cl[2], "money": []}
# 			for z in x['resource']['item']:
# 				cl.append((z['net']['value'], z['net']['code']))
# 				try:
# 					cl.append(x['resource']['encounter']['status'])
# 					cl.append(x['resource']['encounter']['class']['code'])
# 				except KeyError:
# 					cl.append(None)
# 					cl.append(None)

# 				try:
# 					x['resource']['reason'][0]['coding'][0]['display']
# 				except KeyError:
# 					cl.append(None)
# 			cl.append((x['resource']['total']['value'], x['resource']['total']['code']))
# 			clI.append(cl)

