import json
from flask import Flask,render_template, flash,url_for, redirect,request
from flask_sqlalchemy import SQLAlchemy
from tinydb import TinyDB, where, Query
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://iecseman:sierrazulufoxtrotindia@localhost/holocaust"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.secret_key = 'r8YI5oHcl^^aHh1*KklFeQl5Jt2zJMTANyIp9DCua*&qqgm1!I4m)3g5kN6p'
app.config['DEBUG'] = True 
app.jinja_env.add_extension('jinja2.ext.do')
db=SQLAlchemy(app)

class Events(db.Model):
	e_id = db.Column(db.Integer, primary_key = True)
	eventname= db.Column(db.String(100))
	eventpasskey = db.Column(db.String(100))
	jsonstring = db.Column(db.String(5000))

@app.route('/',methods=['GET','POST'])
def index():
	all_events = Events.query.with_entities(Events.eventname)
	passwords = Events.query.with_entities(Events.eventname,Events.eventpasskey)

	password_local = TinyDB('/home/ankit/holocaust2/passwords.db')
	password_local.purge()
	password_dictionary = dict(passwords)
	password_local.insert(password_dictionary)
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
		return redirect('/')

	return render_template("makevent.html")

@app.route('/upload/<eventname>')
def upload(eventname):
	database = TinyDB('/home/ankit/holocaust2/'+eventname+'.db')
	upload_users = database.all()

	for k in upload_users:
		query = "INSERT INTO "+eventname+" ("
		i=0
	  	for l in upload_users[0]:
	  		if i!=0:
	  			query = query + ','
	  		query = query + str(l)
	  		i+=1
	  	query+= ') VALUES ('
	  	i=0
	  	for key in k:
	  		if i!=0:
	  			query = query +','
  			query = query+"'"+str(k[key])+"'"
  			i+=1
		query+= ')'
		db.engine.execute(query)
	db.session.commit()
	database.purge()
	return redirect(url_for('register',eventname = eventname))

@app.route('/register/<eventname>',methods=['GET','POST'])
def register(eventname):
    current_event = Events.query.filter_by(eventname = eventname).first()
    data = json.loads(current_event.jsonstring)
    r_data = data['form_data']['fields']
    database = TinyDB('/home/ankit/holocaust2/'+eventname+'.db')
    databasecopy = TinyDB('/home/ankit/holocaust2/'+eventname+'copy.db')

    if request.method == "POST":
	    data_file = request.form['sender']
	    data =json.loads(data_file)
	    database.insert(data)
	    databasecopy.insert(data)
	    
    upload_users = database.all()
    return render_template("register.html",data=r_data,eventname=eventname, upload_users = upload_users)

@app.route('/verify/<eventname>', methods=['GET','POST'])
def verify(eventname):
	password_local = TinyDB('/home/ankit/holocaust2/passwords.db')
	all_passwords = password_local.all()
	for key in all_passwords[0]:
		if(key == eventname):
			correct_password = all_passwords[0][key]
			
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
	print all_users
	current_event = Events.query.filter_by(eventname = eventname).first()
	data = json.loads(current_event.jsonstring)
	r_data = data ['form_data']['fields']
	return render_template('view.html',all_users = all_users,data = r_data)

@app.route('/delete/<eventname>/<memberid>')
def delete(eventname,memberid):
	database = TinyDB('/home/ankit/holocaust2/'+eventname+'.db')
	databasecopy = TinyDB('/home/ankit/holocaust2/'+eventname+'copy.db')
	database.remove(where('memberid') == memberid)
	databasecopy.remove(where('memberid') == memberid)
	return redirect (url_for('register',eventname = eventname))

try:
	db.create_all()
except Exception, e:
	print "SQL Connection failed"

if __name__ == '__main__':
	app.run()



