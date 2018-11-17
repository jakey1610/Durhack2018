from flask import Flask, render_template, jsonify, request
import os
from jsonServe import basicInfo,Observation,Encounter,mRequest,Goal,Procedure,cPlan,condition,dReport


def search(x):
	users = [] # All the filenames that include 
	direc = './patients/'
	filenames = os.listdir(direc)
	for name in filenames:
		if x in name:
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
	dict["observations"] = Observation(filename)
	dict["encounters"] = Encounter(filename)
	dict["medication_requests"] = mRequest(filename)
	dict["goals"] = Goal(filename)
	dict["procedures"] = Procedure(filename)
	dict["care_plans"] = cPlan(filename)
	dict["condition"] = condition(filename)
	data["patient_data"] = basicInfo(filename)[0]
	data["dict"] = dict
	return jsonify(data)

if __name__ == "__main__":
	app.run(debug=True,host = '127.0.0.1',port = 5000)

