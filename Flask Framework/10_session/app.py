from flask import Flask,request,make_response,session,redirect
from flask.templating import render_template

app = Flask(__name__)

app.secret_key = "a@3#d$56YuQ"

@app.route("/profile")
def profile():
    name_ = session.get("username")
    if name_ == "":
        print(name_,"************")
        return redirect("/login")
    
    return """Welcome {} <br><br> 
    <a href="/logout">logout</a>""".format(name_)
    

@app.route('/login',methods=["POST","GET"])
def login():
    # if request.method == "GET":
        # name_ = request.args.get("name") # args  --> for query string
        # print(name_,"-------------")

        # name_ = request.form.get("name")
    if request.method == "POST":
        name_ = request.form.get("name")
        # response = make_response(render_template("profile.html"))
        # response.set_cookie("username",name_)
        session["username"] = name_
        return render_template("profile.html")

    # if "username" in session:
    #     return "you are already registered"

    return render_template("login.html")

@app.route("/logout")
def logout():
    session.pop("username")
    return redirect("/login")

if __name__ == "__main__":
    app.run(debug=True)

