from flask import Flask, redirect, request, render_template, session, flash
import re
from mysqlconnection import MySQLConnector
app = Flask(__name__)
app.secret_key = "idunno"
mysql = MySQLConnector(app,'email_validation')
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')

@app.route('/')
def index():
	query = "SELECT * FROM email"
	emails = mysql.query_db(query)
	print emails
	return render_template('index.html', all_emails=emails)

@app.route('/submit', methods=['POST'])
def submit():
	if not EMAIL_REGEX.match(request.form['email']):
		flash('Invalid email entry', 'wrong')
		return redirect('/')
	else:
		query = "INSERT INTO email (email, created_at, updated_at) VALUES ( :email, NOW(), NOW());"
		data = {
				'email': request.form['email']
				}
		mysql.query_db(query, data)
		list_emails = "SELECT * FROM email"
		email_list = mysql.query_db(list_emails)
		return render_template('success.html', email_ls=email_list)

app.run(debug=True)