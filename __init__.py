import json
from flask import Flask,render_template, flash, redirect,request
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://ankit:ankitgohel@localhost/flasktest"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.secret_key = 'dfandh jw46tq4t j4yehgwth'
app.config['DEBUG'] = True 
db=SQLAlchemy(app)
@app.route('/holopost',methods=['GET','POST'])
def holopost():
	if request.method == "POST":
		data_file = request.form['penis']
		data = json.load(data_file)
		
@app.route('/index',methods=['GET','POST'])
def index():
	return render_template("index.html")
@app.route('/makevent',methods=['GET','POST'])
def makevent():
	if request.method =="POST":
		data_file = request.form['penis']
		data = json.loads(data_file)
		query = "INSERT INTO events VALUES( default," +"'"+str(data['eventname'])+"'"+","+"'"+str(data['eventpasskey'])+"'"+")"
		i=0
		db.engine.execute(query)
		query = "CREATE TABLE "+" "+data["eventname"]+"("
		for k in data['form_data']['fields']:
			print k

			if i != 0:
				query = query+","

			query=query+str(k['label'].replace(" ","").replace("?","").lower())+" VARCHAR(1000)"
			i+=1
		query = query+")"
		print query
		
		db.engine.execute(query)
		db.session.commit()
		return str(data['form_data'])		

	return render_template("makevent.html")

if __name__ == '__main__':
	app.run()