from flask import Flask, redirect, request, render_template, session, flash
import re
from mysqlconnection import MySQLConnector
from flask_bcrypt import Bcrypt
app = Flask(__name__)
app.secret_key = "idunno"
bcrypt = Bcrypt(app)
mysql = MySQLConnector(app,'login_registration')
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
LETTERS_ONLY = re.compile(r'^[a-zA-Z]*$')


@app.route('/')
def index():
	query = "SELECT * FROM users"
	users = mysql.query_db(query)
	return render_template('index.html', all_users=users)

@app.route('/register', methods=['POST'])
def register():
	errors = []
	if len(request.form['first_name']) < 2:
		errors.append('First name has to have at least 2 characters')
	if not LETTERS_ONLY.match(request.form['first_name']):
		errors.append('First name has to be letters only')
	if len(request.form['first_name']) < 2:
		errors.append('Last name has to have at least 2 characters')
	if not LETTERS_ONLY.match(request.form['last_name']):
		errors.append('Last name has to be letters only')
	if not EMAIL_REGEX.match(request.form['email']):
		errors.append('Invalid email entry')
	if len(request.form['pw']) < 8:
		errors.append('Password must be more than 8 characters')
	if request.form['confirm_pw'] != request.form['pw']:
		errors.append('Please confirm your password')
	if len(errors) > 0:
		for error in errors:
			flash(error)
		return redirect('/')
	else:
		firstname = request.form['first_name']
		lastname = request.form['last_name']
		email = request.form['email']
		password = request.form['pw']
		pw_hash = bcrypt.generate_password_hash(password)
		query = "INSERT INTO users (first_name, last_name, email, password, created_at, updated_at) VALUES (:first_name, :last_name, :email, :password, NOW(), NOW());"
		data = {
				'first_name': firstname,
				'last_name': lastname,
				'email': email,
				'password': pw_hash
				}
		mysql.query_db(query, data)
		return redirect('/')

@app.route('/login', methods=['POST'])
def login():
	errors = []
	if not EMAIL_REGEX.match(request.form['email']):
		errors.append('Invalid email entry')
	if len(request.form['pw']) < 8:
		errors.append('Password must be more than 8 characters')
	if len(errors) > 0:
		for error in errors:
			flash(error)
		return redirect('/')
	else:
		try:
			email = request.form['email']
			password = request.form['pw']
			user_query = "SELECT * FROM users WHERE email = :email LIMIT 1"
			query_data = {'email': email}
			user = mysql.query_db(user_query, query_data)
			if bcrypt.check_password_hash(user[0]['password'], password):
				session['id'] = user[0]['id']
				return redirect('/success')
		except:
			flash('Invalid email or password')
			return redirect('/')

@app.route('/success')
def success():
	query = "SELECT * FROM users WHERE id = :id"
	data = {'id': session['id']}
	user = mysql.query_db(query, data)
	return render_template('successlogin.html', one_user=user)

@app.route('/clear')
def clear():
	session.clear()
	return redirect('/')

app.run(debug=True)