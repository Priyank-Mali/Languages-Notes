from flask import Flask,url_for

app = Flask("__main__")

@app.route("/")
@app.route("/home")
@app.route("/home/<username>")
def dash(username="Guest"):
    return "<h1>Hello World</h1>" + username

with app.test_request_context():
    print(url_for("dash"))
    print(url_for("dash",username="priyank mali"))
    print(url_for("dash",username="priyank mali",password="1234"))
    # print(url_for(""))

"""
/home
/home/priyank%20mali
/home/priyank%20mali?password=1234
"""

if __name__ == "__main__":
    app.run(debug=True)

