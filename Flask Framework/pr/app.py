from flask import Flask

app = Flask(__name__)

@app.route("/home")
def home():
    return "<h1>this is home page</h1>"


if __name__ == "__main__":
    app.run(debug=True)