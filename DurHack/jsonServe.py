import json

def basicInfo(file):
	data = json.load(open(file))
	bI = []
	for x in data['entry']:
		b = []
		y = x['resource']['resourceType']
		if y == "Patient":
			b.append(x['resource']['extension'][0]['valueCodeableConcept']['coding'][0]['display'])
			b.append(x['resource']['extension'][1]['valueCodeableConcept']['coding'][0]['display'])
			b.append(x['resource']['extension'][2]['valueAddress']['city'] + x['resource']['extension'][2]['valueAddress']['state'] + x['resource']['extension'][2]['valueAddress']['country'])
			b.append(x['resource']['extension'][3]['valueString'])
			b.append(x['resource']['extension'][4]['valueCode'])
			b.append(x['resource']['name'][0]['family'] + x['resource']['name'][0]['given'][0])
			b.append(x['resource']['gender'])
			b.append(x['resource']['birthDate'])
			b.append(x['resource']['address'][0]['line'])
			b1 = {"race": b[0], "ethnicity": b[1], "city": b[2], "maidenNames": b[3], "birthSex": b[4], "name": b[5], "gender": b[6], "birthDate": b[7], "address": b[8]}
			bI.append(b1)
	return bI
def Observation(file):
	data = json.load(open(file))
	obs1 = []
	for x in data['entry']:
		y = x['resource']['resourceType']
		if y == 'Observation':
			obs = {}
			try:
				obs['Name'] = x['resource']['code']['text'] #Name  -e.g. BMI
			except:
				obs['Name'] = x['resource']['code']['coding'][0]['display']
			try:
				obs['Value'] = x['resource']['valueQuantity']['value'] #Value of obs
				obs['Unit'] = x['resource']['valueQuantity']['unit']
			except KeyError:
				try:
					obs['Value'] = x['resource']['valueCodeableConcept']['text']
				except KeyError:
					obs['Value'] = ('No Data')
			json.dumps(obs)
			obs1.append(obs)
	print(obs1)
	return obs1

def Encounter(file):
	data = json.load(open(file))
	enc1 =[]
	for x in data['entry']:
		y = x['resource']['resourceType']
		if y == 'Encounter':
			enc = {}
			if x['resource']['class']['code'] == 'outpatient':
				enc['Encounter Type'] = 'outpatient'
				try:
					enc['Date'] = x['resource']['period']['start']
				except KeyError:
					enc['Date'] = 'No Date'
			else:
				try:
					enc['Encounter Reason'] = x['resource']['type']['0']['coding']['text'] #Reason for encounter - e.g. symptom
				except TypeError:
					enc['Encounter Reason'] = x['resource']['type'][0]['text']
				try:
					enc['Outcome'] = x['resource']['reason'][0]['coding'][0]['display']
				except KeyError:
					enc['Outcome'] = 'N/A'
				enc['Date'] = x['resource']['period']['start']
			json.dumps(enc)
			enc1.append(enc)
	print(enc1)
	return enc1

def mRequest(file): #Medication Request
	data = json.load(open(file))
	medreq1 = []
	for x in data['entry']:
		y = x['resource']['resourceType']
		if y == 'MedicationRequest':
			medreq = {}
			medreq['Type of Request'] = x['resource']['extension'][0]['valueCodeableConcept']['text'] #type of request 
			medreq['Medicine'] = x['resource']['medicationCodeableConcept']['text'] #medicine
			medreq['Date'] = x['resource']['authoredOn'] #date
			json.dumps(medreq)
			medreq1.append(medreq)
	return medreq1

def Goal(file):
	data = json.load(open(file))
	goa1 = []
	for x in data['entry']:
		y = x['resource']['resourceType']
		if y == 'Goal':
			goa = {}
			goa['Aim'] = x['resource']['description']['text'] #aim - e.g. less intake
			goa['Progress'] = x['resource']['status'] #progress assessment 
			json.dumps(goa)
			goa1.append(goa)
	print(goa1)
	return goa1

def Procedure(file):
	data = json.load(open(file))
	pro1 = []
	for x in data['entry']:
		y = x['resource']['resourceType']
		if y == 'Procedure':
			pro = {}
			pro['Type'] = x['resource']['code']['text'] # type of procedure
			try:
				pro['Reason'] = x['resource']['reasonReference'][0]['display'] #reason for procedure
			except KeyError:
				pro['Reason'] = 'N/A'
			pro['Status'] = x['resource']['status']
			try:
				pro['Date'] = x['resource']['performedDateTime']
			except KeyError:
				pro['Date'] = x['resource']['performedPeriod']
			json.dumps(pro)
			pro1.append(pro)
	print(pro1)
	return pro1

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
			dI.append(d1 )
	return dI
