from flask import Flask,render_template,request
from pymongo import MongoClient

MONGODB_URI = "mongodb+srv://dada:dada@cluster0-0qy57.mongodb.net/test?retryWrites=true"#i have changed the passw
client = MongoClient(MONGODB_URI)
db = client.get_database("Users")
User = db.Users
"""workers =programmers.estimated_document_count()
print(workers)


testData = {
    "Name": "tes",
    "Res_id": "0",
    "Role": "testcomp",
    "Age": 0
}

workers =programmers.estimated_document_count()
print(workers)"""

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('home.html')

@app.route('/team')
def team():
	return render_template('team.html')     

@app.route('/newAcc', methods=['GET','POST'])
def new_Account():
	if request.method=='GET':
		return render_template('newAcc.html') 
	else:
		print(request.form)
		name = request.form.get('username')
		school = request.form.get('schoolName')
		passwd = request.form.get('password')
		userData = {
		"Name": name,
		"school":school,
		"password":passwd
		}
		return userData
		User.insert_one(userData)




"""@app.route('')
def""" 


@app.route('/profile')  
@app.route('/profile/<name>')
def profile(name=None):
	return render_template('profile.html', name=name)
	
if __name__=='__main__':
	app.run(use_reloader=True,port=4747)