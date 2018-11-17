from flask import Flask, render_template, jsonify, request

from jsonServe import basicInfo,Observation,Encounter,mRequest,Goal,Procedure,cPlan,condition,dReport
app = Flask(__name__)

@app.route('/')
def home():
	return render_template('index.html')

@app.route('/patientSearch',methods = ['POST'])
def patientSearch():	
	searchText = request.values
	data = {}
	dict = {}
	filename = "Abbott701_Veronika555_74.json"
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

