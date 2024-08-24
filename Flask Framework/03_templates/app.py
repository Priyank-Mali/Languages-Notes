from flask import Flask
from flask.templating import render_template
from flask import make_response,redirect
from datetime import datetime

app = Flask("__main__")

@app.route("/")
def deshboard():
    # context = {
    #     "name" : "priyank mali",
    #     "age" : 99,
    #     "time" : datetime.now()
    # }
    name = "priyank"
    age = 99
    return render_template("dashboard.html",context={"name" : name,"age" : age})
    # return render_template("dashboard.html",**context)
    # return render_template("dashboard.html",date=datetime.now())

@app.route("/about")
def about():
    return make_response("This Response is generated by Make Response",201)

@app.route("/contact")
def contact():
    # return redirect("/")
    return redirect("https://www.google.com")

app.run(debug=True)

# if __name__ == "__main__":
#     app.run()