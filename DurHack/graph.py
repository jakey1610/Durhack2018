import json
import os
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import uuid

dirpath = os.getcwd() + '\\patients\\'


def graphChol(person):
	print("running for: "+ dirpath + person)
	filename = 'static/' + str(uuid.uuid4()) + '.png'
	freq = {}
	xcoords = []
	ycoords = []
	failed = []
	z= 0
	c = 0
	for file in os.listdir(dirpath):
		if '.json' in file:
			data = json.load(open(dirpath + file))
			
			for x in data['entry']:
				y = x['resource']['resourceType']
				if y == 'Observation':
					try:
						if "total cholesterol" in x['resource']['code']['coding'][0]['display'].lower():
							ycoords.append(x['resource']['valueQuantity']['value'])
							xcoords.append(c)
							c +=1 
					except KeyError:
						#print(file + ": Fuck off!")
						failed.append(file)
	ycoords.sort()
	data2 = json.load(open(dirpath+person))
	for x in data2['entry']:
		y = x['resource']['resourceType']
		if y == 'Observation':
			try:
				if "total cholesterol" in x['resource']['code']['coding'][0]['display'].lower():
					z = x['resource']['valueQuantity']['value']

			except KeyError:
				print("LIFE")
	if z ==0: 
		return
	plt.annotate(
	# Label and coordinate
	'Patient is here', xy=(ycoords.index(z), z), xytext=(ycoords.index(z), z+100),
	 
	# Custom arrow
	arrowprops=dict(facecolor='black', shrink=0.05)
	)


	
	plt.bar(xcoords, ycoords, 1/1.5,color="blue")
	plt.savefig(filename)
	plt.close('all')
	return filename

def graphSodium(person):
	filename = 'static/' + str(uuid.uuid4()) + '.png'
	z= 0
	freq = {}
	xcoords = []
	ycoords = []
	failed = []
	c = 0
	for file in os.listdir(dirpath):
		if '.json' in file:
			data = json.load(open(dirpath + file))
			
			for x in data['entry']:
				y = x['resource']['resourceType']
				if y == 'Observation':
					try:
						if "sodium" in x['resource']['code']['coding'][0]['display'].lower():
							ycoords.append(x['resource']['valueQuantity']['value'])
							xcoords.append(c)
							c +=1 
					except KeyError:
						#print(file + ": Fuck off!")
						failed.append(file)
	ycoords.sort()
	data2 = json.load(open(dirpath+person))
	for x in data2['entry']:
		y = x['resource']['resourceType']
		if y == 'Observation':
			try:
				if "sodium" in x['resource']['code']['coding'][0]['display'].lower():
					z = x['resource']['valueQuantity']['value']

			except KeyError:
				print("LIFE")
	if z ==0:
		return
	plt.annotate(
	# Label and coordinate
	'Patient is here', xy=(ycoords.index(z), z), xytext=(ycoords.index(z), z+10),
	 
	# Custom arrow
	arrowprops=dict(facecolor='black', shrink=0.05)
	)
	plt.axis([0,xcoords[-1],50,155])
	plt.xlabel('Cumulative patient count')
	plt.bar(xcoords, ycoords, 1/1.5,color="red")
	plt.savefig(filename)
	plt.close('all')
	return filename

def graphCalc(person):
	filename = 'static/' + str(uuid.uuid4()) + '.png'
	freq = {}
	xcoords = []
	ycoords = []
	failed = []
	z= 0
	c = 0
	for file in os.listdir(dirpath):
		if '.json' in file:
			data = json.load(open(dirpath + file))
			
			for x in data['entry']:
				y = x['resource']['resourceType']
				if y == 'Observation':
					try:
						if "calcium" in x['resource']['code']['coding'][0]['display'].lower():
							ycoords.append(x['resource']['valueQuantity']['value'])
							xcoords.append(c)
							c +=1 
					except KeyError:
						#print(file + ": Fuck off!")
						failed.append(file)
	ycoords.sort()
	data2 = json.load(open(dirpath+person))
	for x in data2['entry']:
		y = x['resource']['resourceType']
		if y == 'Observation':
			try:
				if "calcium" in x['resource']['code']['coding'][0]['display'].lower():
					z = x['resource']['valueQuantity']['value']

			except KeyError:
				print("LIFE")
	if z ==0: 
		return
	plt.annotate(
	# Label and coordinate
	'Patient is here', xy=(ycoords.index(z), z), xytext=(ycoords.index(z)-400, z+1.5),
	 
	# Custom arrow
	arrowprops=dict(facecolor='black', shrink=0.05)
	)
	plt.axis([0,xcoords[-1],5,12])
	plt.xlabel('Cumulative patient count')
	plt.bar(xcoords, ycoords, 1/1.5,color="green")
	plt.savefig(filename)
	plt.close('all')
	return filename