import json
from flask import Flask,render_template, flash, redirect,request
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://iecseman:sierrazulufoxtrotindia@localhost/holocaust"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.secret_key = 'r8YI5oHcl^^aHh1*KklFeQl5Jt2zJMTANyIp9DCua*&qqgm1!I4m)3g5kN6p'
app.config['DEBUG'] = True 
db=SQLAlchemy(app)
@app.route('/index',methods=['GET','POST'])
def index():
	return render_template("index.html")
@app.route('/makevent',methods=['GET','POST'])
def makevent():
	if request.method =="POST":
		data_file = request.form['sender']
		data = json.loads(data_file)
		query = "INSERT INTO events VALUES( default," +"'"+str(data['eventname'])+"'"+","+"'"+str(data['eventpasskey'])+"'"+")"
		i=0
		db.engine.execute(query)
		query = "CREATE TABLE "+" "+data["eventname"]+"("
		for k in data['form_data']['fields']:
			if i != 0:
				query = query+","
			query=query+str(k['label'].replace(" ","").replace("?","").lower())+" VARCHAR(1000)"
			i+=1
		query = query+")"
		db.engine.execute(query)
		db.session.commit()
		return str(data['form_data'])		
	return render_template("makevent.html")
if __name__ == '__main__':
	app.run()