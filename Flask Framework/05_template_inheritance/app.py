from flask import Flask
from flask.templating import render_template
from flask import make_response,redirect

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")


if __name__ == "__main__":
    app.run(debug=True)
    # app.run()