import json

def basicInfo(file):
	data = json.load(file)
	bI = []
	for x in data['entry']:
		b = []
		y = x['resource']['resourceType']
		if y == "Patient":
			b.append(x['resource']['extension'][0]['valueCodeableConcept']['coding'][0]['display'])
			b.append(x['resource']['extension'][1]['valueCodeableConcept']['coding'][0]['display'])
			b.append(x['resource']['extension'][2]['valueAddress'])
			b.append(x['resource']['extension'][3]['valueString'])
			b.append(x['resource']['extension'][4]['valueCode'])
			b.append(x['resource']['name'][0])
			b.append(x['resource']['gender'])
			b.append(x['resource']['birthDate'])
			b.append(x['resource']['address'][0]['line'])
			b1 = {"race": b[0], "ethnicity": b[1], "city": b[2], "maidenNames": b[3], "birthSex": b[4], "name": b[5], "gender": b[6], "birthDate": b[7], "address": b[8]}
			b1 = json.dumps(b1)
			bI.append(b1)
	return bI