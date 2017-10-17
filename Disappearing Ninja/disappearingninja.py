from flask import Flask, render_template, redirect, session, request, flash
app = Flask(__name__)
app.secret_key = "itsasecret"

@app.route('/')
def root():
	return "No ninjas here"

@app.route('/ninjas')
def turtles():
	return render_template('index.html')

@app.route('/ninjas/<color>')
def ninjas(color):
	ninja = str(color)
	if ninja == "blue":
		return render_template('ninjas.html', turtle="leonardo")
	elif ninja == "purple":
		return render_template('ninjas.html', turtle="donatello")
	elif ninja == "orange":
		return render_template('ninjas.html', turtle="michelangelo")
	elif ninja == "red":
		return render_template('ninjas.html', turtle="raphael")
	else:
		return render_template('ninjas.html', turtle="notapril")
app.run(debug=True)