from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/result', methods=["GET", "POST"])
def submit():
    return render_template("result.html", name=request.form["your_name"], dojoloc=request.form["dojo_loc"], favlang=request.form["fav_lang"], comments=request.form["comments"])
app.run(debug=True)
