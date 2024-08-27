from flask import Flask,render_template,request,abort
from http import HTTPStatus

app = Flask(__name__)

@app.route("/printStatus/")
def printStatus():
    # print(list(HTTPStatus))
    name_ = request.args.get("name")
    if name_ == "admin":
        return render_template("status.html",status=list(HTTPStatus))
    else:
        # abort(403)
        abort(500)

if __name__ == "__main__":
    app.run(debug=True) 