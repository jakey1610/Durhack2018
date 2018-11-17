from flask import Flask, render_template, jsonify, request
import basicInfo

app = Flask(__name__)

@app.route('/')
def home():
	return render_template('index.html')

@app.route('/patientSearch',methods = ['POST'])
def patientSearch():	
	searchText = request.form['searchText']
	return jsonify({})

if __name__ == "__main__":
	app.run(debug=True,host = '127.0.0.1',port = 5000)

