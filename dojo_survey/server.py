from flask import Flask, render_template, request, redirect, request, flash, session
app = Flask(__name__)
app.secret_key= "mermaids"

@app.route('/')
def index ():
	
	return render_template('index.html')

@app.route('/results', methods= ['POST'])
def results():
	if len(request.form['name']) < 1:
		flash ('Name Required')
	else:
		flash ('Great, your name is {}').format(request.form['name'])
	return render_template('results.html', user = request.form)

app.run(debug=True)
