import json
import numpy as np
import os

def flags(person):
	#Return the boolean values for each; whether above 98th percentile or below the 2nd percentile for sodium, total cholesterol, and calcium.
	#flags order is cholesterol, sodium, and calcium
	flags = [False, False, False]
	chol, sod, cal = [],[],[]
	for file in os.listdir('C:/Users/Jake Mortimer/Downloads/fhir'):
		if '.json' in file:
			data = json.load(open('C:/Users/Jake Mortimer/Downloads/fhir/' + file)) 
			for x in data['entry']:
				y = x['resource']['resourceType']
				if y == 'Observation':
					try:
						if "total cholesterol" in x['resource']['code']['coding'][0]['display'].lower():
							chol.append(x['resource']['valueQuantity']['value'])
						elif "sodium" in x['resource']['code']['coding'][0]['display'].lower():
							sod.append(x['resource']['valueQuantity']['value'])
						elif "calcium" in x['resource']['code']['coding'][0]['display'].lower():
							cal.append(x['resource']['valueQuantity']['value'])
					except KeyError:
						#print(file + ": Fuck off!")
						failed.append(file)
	chol.sort()
	chola = np.array(chol)
	chol98 = np.percentile(chola, 98)
	chol2 = np.percentile(chola, 2)
	sod.sort()
	soda = np.array(sod)
	sod98 = np.percentile(soda, 98)
	sod2 = np.percentile(soda, 2)
	cal.sort()
	cala = np.array(cal)
	cal98 = np.percentile(cala, 98)
	cal2 = np.percentile(cala, 2)

	data2 = json.load(open('C:/Users/Jake Mortimer/Downloads/fhir/'+person))
	for x in data2['entry']:
		y = x['resource']['resourceType']
		if y == 'Observation':
			try:
				if "calcium" in x['resource']['code']['coding'][0]['display'].lower():
					z = x['resource']['valueQuantity']['value']
					if z > cal98 or z < cal2:
						flags[2] = True
				if "sodium" in x['resource']['code']['coding'][0]['display'].lower():
					z = x['resource']['valueQuantity']['value']
					if z > sod98 or z < sod2:
						flags[1] = True
				if "cholesterol" in x['resource']['code']['coding'][0]['display'].lower():
					z = x['resource']['valueQuantity']['value']
					if z > chol98 or z < chol2:
						flags[0] = True
			except KeyError:
				print("LIFE")
	return flags

print(flags("Abbott701_Veronika555_74.json"))

