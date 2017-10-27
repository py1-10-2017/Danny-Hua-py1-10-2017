from flask import Flask, redirect, request, render_template, session, flash
import re
from mysqlconnection import MySQLConnector
app = Flask(__name__)
app.secret_key = "idunno"
mysql = MySQLConnector(app,'full_friends')
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')


# def validation():
# 	if request.form['first_name'] == '':
# 		flash('Invalid first name', 'error')
# 		return redirect('/')
# 	elif request.form['last_name'] == '':
# 		flash('Invalid last_name', 'error')
# 		return redirect('/')
# 	elif not EMAIL_REGEX.match(request.form['email']):
# 		flash('Invalid email', 'error')
# 		return redirect('/')
# 	else:
# 		return redirect('/')

@app.route('/')
def index():
	query = "SELECT * FROM users"
	users = mysql.query_db(query)
	print users
	return render_template('index.html', all_users=users)

@app.route('/friends', methods=['POST'])
def add():
	if request.form['first_name'] == '':
		flash('Invalid first name', 'error')
		return redirect('/')
	elif request.form['last_name'] == '':
		flash('Invalid last_name', 'error')
		return redirect('/')
	elif not EMAIL_REGEX.match(request.form['email']):
		flash('Invalid email', 'error')
		return redirect('/')
	else:
		query = "INSERT INTO users (first_name, last_name, email, created_at, updated_at) VALUES (:first_name, :last_name, :email, NOW(), NOW());"
		data = {
				'first_name': request.form['first_name'],
				'last_name': request.form['last_name'],
				'email': request.form['email']
				}
		mysql.query_db(query, data)
		return redirect('/')

@app.route('/friends/<id>/edit')
def edit(id):
	query = "SELECT * FROM users WHERE id = :id"
	data = {'id': id}
	friend_id = mysql.query_db(query, data)
	# print friend_id[0]
	# return "friends" + id + "edit"
	return render_template('edit.html', one_friend=friend_id)

@app.route('/friends/<id>', methods=['POST'])
def update(id):
	if request.form['first_name'] == '':
		flash('Invalid first name', 'error')
		return redirect('friends/' + id + '/edit')
	elif request.form['last_name'] == '':
		flash('Invalid last_name', 'error')
		return redirect('friends/' + id + '/edit')
	elif not EMAIL_REGEX.match(request.form['email']):
		flash('Invalid email', 'error')
		return redirect('friends/' + id + '/edit')
	else:
		query = "UPDATE users SET first_name = :first_name, last_name = :last_name, email = :email, updated_at = NOW() WHERE id = :id"
		data = {
				'first_name': request.form['first_name'],
				'last_name': request.form['last_name'],
				'email': request.form['email'],
				'id': id
				}
		mysql.query_db(query, data)
		return redirect('/')

@app.route('/friends/<id>/delete', methods=['POST'])
def delete(id):
	query = "DELETE FROM users WHERE id = :id"
	data = {'id': id}
	mysql.query_db(query, data)
	return redirect('/')

app.run(debug=True)