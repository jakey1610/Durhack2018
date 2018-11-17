
import json
import os
import matplotlib.pyplot as plt

freq = {}
xcoords = []
ycoords = []
failed = []
for file in os.listdir('C:/Users/Jake Mortimer/Downloads/fhir'):
	if '.json' in file:
		data = json.load(open('C:/Users/Jake Mortimer/Downloads/fhir/' + file))
		for x in data['entry']:
			count1 = 0
			y = x['resource']['resourceType']
			if y == 'Observation':
				try:
					if "systolic" in x['resource']['component'][0]['code']['text'].lower():
						xcoords.append(x['resource']['component'][0]['valueQuantity']['value'])
						count1 += 1
				except KeyError:
					#print(file + ": Fuck off!")
					failed.append(file)
		for x in data['entry']:
			y = x['resource']['resourceType']
			if y == 'Observation':
				try:
					if "hemoglobin" in x['resource']['code']['coding'][0]['display'].lower() and count1 == 1:
						ycoords.append(x['resource']['valueQuantity']['value'])
				except KeyError:
					#print(file + ": Fuck off!")
					failed.append(file)
				if count1 = 0:
					del xcoords[-1]


print(failed)
plt.plot(xcoords, ycoords)
plt.show()