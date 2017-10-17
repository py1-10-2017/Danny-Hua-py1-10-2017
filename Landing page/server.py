from flask import Flask, render_template, request
app = Flask(__name__)
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/ninjas')
def ninjas():
    return render_template("ninjas.html")

@app.route('/form')
def form():
    return render_template("form.html")

@app.route('/dojos/new', methods=["POST"])
def dojos():
    print request.form["favorite_ninja"]
    return render_template("ninjas.html", x=request.form["favorite_ninja"])
    return "you are in dojos/new"
app.run(debug=True)
