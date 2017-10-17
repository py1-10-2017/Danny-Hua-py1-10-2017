from flask import Flask, render_template, request, redirect, session, flash
app = Flask(__name__)
app.secret_key = "notsosecret"

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/result', methods=["GET", "POST"])
def submit():
	if len(request.form['your_name']) < 1 and len(request.form['comments']) < 1:
		flash("You have no name and no comments")
		return redirect('/')
	elif len(request.form['your_name']) < 1:
		flash("You must put in a name!")
		return redirect('/')
	elif len(request.form['comments']) < 1:
		flash("You must put in a comment")
		return redirect('/')
	elif len(request.form['comments']) > 120:
		flash("Your comments is over 120 characters. It is too long!")
		return redirect('/')
	else:
		flash("You have enter {} as your name".format(request.form['your_name']))
		return render_template("result.html", name=request.form["your_name"], dojoloc=request.form["dojo_loc"], favlang=request.form["fav_lang"], comments=request.form["comments"])

app.run(debug=True)
