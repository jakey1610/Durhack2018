import json 
from pprint import pprint

with open('/Users/Sami/Desktop/DurHack/test2.json') as x:
	data = json.load(x)

rtypes = []

for x in data['entry']:
	y = x['resource']['resourceType']
	# rtypes.append(y)
	obs = {}
	enc = {}
	medreq = {}
	goa = {}
	pro = {}
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
		print(json.dumps(obs))
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
		print(json.dumps(pro))
