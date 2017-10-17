from flask import Flask, render_template, request, session, redirect
from datetime import datetime
app = Flask(__name__)
app.secret_key = "havenoidea"

import random

@app.route('/')
def index():
	if "gold" not in session:
		session["gold"] = 0
		session["activities"] = []
	return render_template('index.html')

@app.route('/process_money', methods=["POST"])
def process():
	date = datetime.now().strftime("%A, %d. %B %Y %I:%M%p")
	places = request.form["place"]
	if places == "farm":
		money = random.randint(10, 20)
		session["gold"] += money
		session["activities"].append({"act": "Earn {} gold from the {}! ".format(money,places), "class":"win", "time":date})
	elif places  == "cave":
		money = random.randint(5, 10)
		session["gold"] += money
		session["activities"].append({"act": "Earn {} gold from the {}! ".format(money,places), "class":"win", "time":date})
	elif places  == "house":
		money = random.randint(2, 5)
		session["gold"] += money
		session["activities"].append({"act": "Earn {} gold from the {}! ".format(money,places), "class":"win", "time":date})
	else:
		money = random.randint(-50, 50)
		if money > 0:
			session["activities"].append({"act": "Earn {} gold from the {}! ".format(money,places), "class":"win", "time":date})
		else:
			session["activities"].append({"act": "Loss {} gold from the {}! ".format(money,places), "class":"loss", "time":date})
	session["gold"] += money
	return redirect('/')

@app.route('/reset')
def reset():
	session.clear()
	return redirect('/')

app.run(debug=True)