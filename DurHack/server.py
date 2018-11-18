from flask import Flask, render_template, jsonify, request
import os
from jsonServe import basicInfo,Observation,Encounter,mRequest,Goal,Procedure,cPlan,condition,dReport
from graph import graphChol, graphSodium, graphCalc
from flags import calcFlags

pngs = []

def search(x):
	users = [] # All the filenames that include 
	direc = './patients/'
	filenames = os.listdir(direc)
	for name in filenames:
		if x.lower() in name.lower():
			users.append(name[:-5])
	return users

app = Flask(__name__)

@app.route('/')
def home():
	return render_template('index.html')

@app.route('/patientSearch',methods = ['POST'])
def patientSearch():	
	searchText = request.form.get('searchName')
	patients = search(searchText)
	userJson = {}
	array = []
	for p in patients:
		array.append({"name":p})
	userJson["patients"] = array
	return jsonify(userJson)


@app.route('/patientData',methods = ['POST'])
def patientData():
	data = {}
	dict = {}
	fn = request.form.get("filename")
	filename = "./patients/" + fn.strip() + '.json'
	dict["Observations"] = Observation(filename)
	dict["Encounters"] = Encounter(filename)
	dict["Medication Requests"] = mRequest(filename)
	dict["Goals"] = Goal(filename)
	dict["Procedures"] = Procedure(filename)
	dict["Care Plans"] = cPlan(filename)
	dict["Condition"] = condition(filename)
	dict["Diagnostic Report"] = dReport(filename)
	data["patient_data"] = basicInfo(filename)[0]
	data["dict"] = dict
	patient_flags = calcFlags(fn.strip() + '.json')
	data["flags"] = {}
	for i, name in enumerate(["cholesterol", "sodium", "calcium"]):
		data["flags"][name] = patient_flags[i]
	return jsonify(data)

#renders images that show analysis of our data
@app.route('/analysis')
def analysis():
	fn = request.values.get("filename")
	filename = fn.strip() + '.json'
	#remove previous files
	for item in pngs:
		if item is not None:
			os.remove(item)
	del pngs[:]

	cholFile = graphChol(filename)
	calcFile = graphCalc(filename)
	sodiFile = graphSodium(filename)
	pngs.extend([
		cholFile,
		calcFile,
		sodiFile,
	])
	return render_template('analysis.html', cholFile=cholFile, calcFile=calcFile, sodiFile=sodiFile)

if __name__ == "__main__":
	app.run(debug=True,host = '127.0.0.1',port = 5000)

