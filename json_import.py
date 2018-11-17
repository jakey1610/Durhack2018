import json 
from pprint import pprint

with open('/Users/Sami/Desktop/DurHack/test.json') as x:
	data = json.load(x)

rtypes = []

for x in data['entry']:
	y = x['resource']['resourceType']
	# rtypes.append(y)
	""" if y == 'Observation':
		try:
			print(x['resource']['code']['text']) #Name  -e.g. BMI
		except:
			print(x['resource']['code']['coding'][0]['display'])
		try:
			print(x['resource']['valueQuantity']['value']) #Value of obs
			print(x['resource']['valueQuantity']['unit'])
		except KeyError:
			try:
				print(x['resource']['valueCodeableConcept']['text'])
			except KeyError:
				print('No Data')
	if y == 'Encounter':
		if x['resource']['class']['code'] == 'outpatient':
			print('outpatient')
			try:
				print(x['resource']['class']['period']['start'])
			except KeyError:
				print('No Date')
		else:
			try:
				print(x['resource']['type']['0']['coding']['text']) #Reason for encounter - e.g. symtpom
			except TypeError:
				print(x['resource']['type'][0]['text'])
			try:
				print(x['resource']['reason'][0]['coding'][0]['display'])
			except KeyError:
				print('N/A')
			print(x['resource']['period']['start']) """
	if y == 'MedicationRequest':
		print(x['resource']['extension'][0]['valueCodeableConcept']['text']) #type of request 
		print(x['resource']['medicationCodeableConcept']['text']) #medicine
		print(x['resource']['authoredOn']) #date

