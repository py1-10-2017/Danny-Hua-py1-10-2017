from flask import Flask, render_template, request, session, redirect
app = Flask(__name__)
app.secret_key = "idunno"

import random

@app.route('/')
def index():
	if "num" not in session:
		session["num"] = random.randrange(0, 101)
	return render_template('index.html')

@app.route('/process', methods=["POST"])
def process():
	if int(request.form["action"]) == session["num"]:
		session["current_number"] = "correct"
	elif int(request.form["action"]) > session["num"]:
		session["current_number"] = "high"
	else:
		session["current_number"] = "low"
	return render_template('result.html')

@app.route('/reset')
def reset():
	session.clear()
	return redirect('/')

app.run(debug=True)