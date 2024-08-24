from flask import Flask
from flask import make_response
from flask.templating import render_template
from datetime import datetime

app = Flask(__name__)

@app.route("/",methods=["GET","POST"])
def home():
    context = {
        "name" : "priyank",
        "date" : datetime.now()
    }
    return render_template("home.html",**context)

@app.route("/check")
def check():
    return render_template("check.html")   


app.run(debug=True)

