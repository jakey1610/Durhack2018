import json 
from pprint import pprint

"""with open('/Users/Sami/Desktop/DurHack/test2.json') as x:
	data = json.load(x)

rtypes = []
obs1 = []

for x in data['entry']:
	y = x['resource']['resourceType']
	# rtypes.append(y)
	enc = {}
	medreq = {}
	goa = {}
	pro = {}
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
	if y == 'Encounter':
		if x['resource']['class']['code'] == 'outpatient':
			enc['Encounter Type'] = 'outpatient'
			try:
				enc['Date'] = x['resource']['class']['period']['start']
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
		print(json.dumps(enc))
	if y == 'MedicationRequest':
		medreq['Type of Request'] = x['resource']['extension'][0]['valueCodeableConcept']['text'] #type of request 
		medreq['Medicine'] = x['resource']['medicationCodeableConcept']['text'] #medicine
		medreq['Date'] = x['resource']['authoredOn'] #date
		print(json.dumps(medreq)) 
	if y == 'Goal':
		goa['Aim'] = x['resource']['description']['text'] #aim - e.g. less intake
		goa['Progress'] = x['resource']['status'] #progress assessment 
		print(json.dumps(goa))
	if y == 'Procedure':
		pro['Type'] = x['resource']['code']['text'] # type of procedure
		try:
			pro['Reason'] = x['resource']['reasonReference'][0]['display'] #reason for procedure
		except KeyError:
			pro['Reason'] = 'N/A'
		pro['Status'] = x['resource']['status']
		pro['Date'] = x['resource']['performedDateTime']
		print(json.dumps(pro)) """

def Observation(file):
	data = json.load(file)
	obs1 = []
	for x in data['entry']:
		y = x['resource']['resourceType']
		obs = {}
		if y == 'Observation':
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
	return obs1

def Encounter(file):
	data = json.load(file)
	enc1 =[]
	for x in data['entry']:
		y = x['resource']['resourceType']
		enc = {}
		if y == 'Encounter':
			if x['resource']['class']['code'] == 'outpatient':
				enc['Encounter Type'] = 'outpatient'
				try:
					enc['Date'] = x['resource']['class']['period']['start']
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
	return enc1

def mRequest(file): #Medication Request
	data = json.load(file)
	medreq1 = []
	for x in data['entry']:
		y = x['resource']['resourceType']
		medreq = {}
		if y == 'MedicationRequest':
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
		goa = {}
		if y == 'Goal':
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
		pro = {}
		if y == 'Procedure':
			pro['Type'] = x['resource']['code']['text'] # type of procedure
			try:
				pro['Reason'] = x['resource']['reasonReference'][0]['display'] #reason for procedure
			except KeyError:
				pro['Reason'] = 'N/A'
			pro['Status'] = x['resource']['status']
			pro['Date'] = x['resource']['performedDateTime']
			json.dumps(pro)
			pro1.append(pro)
	print(pro1)
	return pro1

Goal('/Users/Sami/Desktop/DurHack/test2.json')