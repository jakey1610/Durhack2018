import json
import os
import matplotlib.pyplot as plt

freq = {}
xcoords = []
ycoords = []

for file in os.listdir('/Users/Sami/Desktop/fhir'):
	if '.json' in file:
		print(file)
		data = json.load(open('/Users/Sami/Desktop/fhir/' + file))

		age = file.split('_')[2].split('.')[0]
		for x in data['entry']:
			y = x['resource']['resourceType']
			if y == 'Condition':
				if 'cancer' in x['resource']['code']['coding'][0]['display'].lower():
					try:
						freq[age] +=1
					except KeyError:
						freq[age] = 1

for i in freq.keys():
	xcoords.append(float(i))
	ycoords.append(float(freq[i]))

plt.plot(xcoords, ycoords)