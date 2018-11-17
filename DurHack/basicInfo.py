import json
with open('Abbott701_Veronika555_74.json') as x:
	data = json.load(x)
bI = []
for x in data['entry']:
	b = []
	y = x['resource']['resourceType']
	if y == "Patient":
		for z in range(2):
			b.append(x['resource']['extension'][z]['valueCodeableConcept']['coding'][0]['display'])
		b.append(x['resource']['extension'][2]['valueAddress'])
		b.append(x['resource']['extension'][3]['valueString'])
		b.append(x['resource']['extension'][4]['valueCode'])
		b.append(x['resource']['name'])
		b.append(x['resource']['gender'])
		b.append(x['resource']['birthDate'])
		b.append(x['resource']['address'][0]['line'])
		bI.append(b)
print(bI)
		