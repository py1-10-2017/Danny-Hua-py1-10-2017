from flask import Flask, redirect, request, render_template, session, flash
import re
from mysqlconnection import MySQLConnector
from flask_bcrypt import Bcrypt
app = Flask(__name__)
app.secret_key = "idunno"
bcrypt = Bcrypt(app)
mysql = MySQLConnector(app,'danny_the_wall')
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
LETTERS_ONLY = re.compile(r'^[a-zA-Z]*$')

@app.route('/')
def index():
	query = 'SELECT * FROM users'
	users = mysql.query_db(query)
	return render_template('index.html')

@app.route('/register', methods=['POST'])
def register():
	errors = [];

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
		errors.append('Password must be 8 characters or more')

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
	if not EMAIL_REGEX.match(request.form['email']):
		flash('Invalid email entry')
		return redirect('/')
	elif len(request.form['pw']) < 8:
		flash('Password must be 8 characters or more')
		return redirect('/')
	else:
		try:
			email = request.form['email']
			password = request.form['pw']
			query = 'SELECT * FROM users WHERE email = :email LIMIT 1'
			data = {'email': email}
			user = mysql.query_db(query, data)
			if bcrypt.check_password_hash(user[0]['password'], password):
				session['id'] = user[0]['id']
				return redirect('/success')
			else:
				flash('Invalid user or password')
				return redirect('/')
		except:
			flash('Invalid user or password')
			return redirect('/')

@app.route('/success')
def success():
	comment_query = "SELECT users.id, users.first_name, users.last_name, comments.message_id, comments.comment, date_format(comments.created_at, '%M %d, %Y') AS 'comment_date' FROM comments LEFT JOIN users ON comments.user_id = users.id"
	comments = mysql.query_db(comment_query)
	print comments

	message_query = "SELECT messages.id AS message_id, messages.message, date_format(messages.created_at, '%M %d, %Y') AS 'message_date', users.id, users.first_name, users.last_name FROM messages LEFT JOIN users ON messages.user_id = users.id"
	messages = mysql.query_db(message_query)

	user_query = "SELECT users.id, users.first_name, users.last_name FROM users WHERE users.id = :id"
	user_data = {'id': session['id']}
	user = mysql.query_db(user_query, user_data)[0]

	context = {
		'comments': comments,
		'one_user': user,
		'messages': messages
	}

	return render_template('thewall.html', context=context)

@app.route('/post/<current_user>', methods=['POST'])
def post(current_user):
	query = "INSERT INTO messages (message, created_at, updated_at, user_id) VALUES (:message, NOW(), NOW(), :user_id);"
	data = {
			'message': request.form['message'],
			'user_id': current_user
			}
	mysql.query_db(query, data)
	return redirect('/success')

@app.route('/comment/<current_message>', methods=['POST'])
def comment(current_message):
	query = "INSERT INTO comments (comment, created_at, updated_at, message_id, user_id) VALUES (:comment, NOW(), NOW(), :message_id, :user_id);"
	data = {
			'comment': request.form['comment'],
			'message_id': current_message,
			'user_id': session['id']
			}
	mysql.query_db(query, data)
	return redirect('/success')

@app.route('/del_message/<message_id>', methods=['POST'])
def del_message(message_id):
	query = "DELETE FROM messages WHERE id = :id"
	data = {'id': message_id}
	mysql.query_db(query, data)
	return redirect('/success')

@app.route('/logout')
def logout():
	session.clear()
	return redirect('/')

app.run(debug=True)