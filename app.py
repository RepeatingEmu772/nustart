from flask import Flask,render_template
app = Flask(__name__)

@app.route('/')
def index():
	return render_template('home.html')

@app.route('/profile')  
@app.route('/profile/<name>')
def profile(name=None):
	return render_template('profile.html', name=name)


	
if __name__=='__main__':
	app.run(use_reloader=True)