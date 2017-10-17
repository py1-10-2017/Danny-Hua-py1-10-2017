from flask import Flask, render_template, session, redirect, flash, request
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
PASS_REGEX = re.compile(r'^(?=.*[A-Z])(?=.*[0-9])')

app = Flask(__name__)
app.secret_key = "veryclassified"

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
	if len(request.form['first_name']) < 1 or not request.form['first_name'].isalpha():
		flash("First name cannot be blank or have numbers", "error")
		return redirect('/')
	elif len(request.form['last_name']) < 1 or not request.form['last_name'].isalpha():
		flash('Last name cannot be blank or have numbers', 'error')
		return redirect('/')
	elif len(request.form['email']) < 1:
		flash('Email cannot be blank', 'error')
		return redirect('/')
	elif not EMAIL_REGEX.match(request.form['email']):
		flash('Invalid email entry', 'error')
		return redirect('/')
	elif len(request.form['password']) < 1:
		flash('Password cannot be blank', 'error')
		return redirect('/')
	elif not PASS_REGEX.match(request.form['password']):
		flash('Password must contain one uppercase and one number')
		return redirect('/')
	elif len(request.form['password']) < 8:
		flash('Password must be more than 8 characters', 'error')
		return redirect('/')
	elif request.form['confirm_password'] != request.form['password']:
		flash('Please confirm your password', 'error')
		return redirect('/')
	else:
		flash('Everything looks good')
		return "Everything pass"

app.run(debug=True)