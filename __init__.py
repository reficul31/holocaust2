import json
from flask import Flask,render_template, flash,url_for, redirect,request
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://iecseman:sierrazulufoxtrotindia@localhost/holocaust"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.secret_key = 'r8YI5oHcl^^aHh1*KklFeQl5Jt2zJMTANyIp9DCua*&qqgm1!I4m)3g5kN6p'
app.config['DEBUG'] = True 
db=SQLAlchemy(app)

class Events(db.Model):
	e_id = db.Column(db.Integer, primary_key = True)
	eventname= db.Column(db.String(100))
	eventpasskey = db.Column(db.String(100))
	jsonstring = db.Column(db.String(5000))

@app.route('/',methods=['GET','POST'])
def index():
	all_events = Events.query.with_entities(Events.eventname)
	return render_template("index.html",all_events = all_events)

@app.route('/make/event',methods=['GET','POST'])
def makevent():
	if request.method =="POST":
		data_file = request.form['sender']
		data = json.loads(data_file)
		query = "INSERT INTO events VALUES( default," +"'"+str(data['eventname'])+"'"+","+"'"+str(data['eventpasskey'])+"'"+","+"'"+str(data_file)+"'"+")"
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
	return render_template("makevent.html")

@app.route('/register/<eventname>',methods=['GET','POST'])
def register(eventname):
    current_event = Events.query.filter_by(eventname = eventname).first()
    data = json.loads(current_event.jsonstring)
    r_data = data['form_data']['fields']

    if request.method == "POST":
            data_file = request.form['sender']
            data =json.loads(data_file)
            query = "INSERT INTO "+eventname+" ("
            i=0
            for k in data:
                if i !=0:
                    query = query +','
                query = query+str(k)	
                i+=1
            query+= ') VALUES ('
            i=0
            for k in data:
                if i !=0:
                    query = query +','
                query = query+"'"+str(data[k])+"'"
                i+=1
            query+= ')'
            db.engine.execute(query)
            db.session.commit()
    return render_template("register.html",data=r_data,eventname=eventname)

@app.route('/verify/<eventname>', methods=['GET','POST'])
def verify(eventname):
	current_event = Events.query.filter_by(eventname = eventname).first()
	correct_password = current_event.eventpasskey

	if request.method == 'GET':
		return render_template("verify.html",eventname = eventname)
	elif request.method == 'POST':
		if(request.form['passkey'] == correct_password):
			return redirect(url_for('register',eventname = eventname))
		else:
			return redirect('/')

@app.route('/view/<eventname>')
def view(eventname):
	query = 'SELECT * FROM ' + eventname
	all_users = db.engine.execute(query)
	current_event = Events.query.filter_by(eventname = eventname).first()
	data = json.loads(current_event.jsonstring)
	r_data = data ['form_data']['fields']
	return render_template('view.html',all_users = all_users,data = r_data)

try:
	db.create_all()
except Exception, e:
	print "SQL Connection failed"

if __name__ == '__main__':
	app.run()

