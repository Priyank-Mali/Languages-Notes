from flask import Flask,request,redirect,url_for,make_response
from flask.templating import render_template

app = Flask(__name__)

# @app.route("/login",methods=["POST","GET"])
# def login():
#     if request.method == "POST":
#         name_ = request.form.get("name")
#         response = redirect("/profile")
#         response.set_cookie("username",name_)
#         return response
#         # return redirect("/profile")
#         # or
        # return redirect(url_for("profile"))
    # return render_template("login.html")

# @app.route("/profile")
# def profile():
#     return render_template("profile.html")

#---------------------------------------------------------
"""
In Flask, cookies are set on response object. Use make_response() function to get response object from return value of a view function. After that, use the set_cookie() function of response object to store a cookie.
"""
@app.route("/login",methods=["POST","GET"])
def login():
    if request.method == "POST":
        name_ = request.form.get("name")
        response = make_response(render_template("profile.html"))
        response.set_cookie("username",name_)
        return response
    return render_template("login.html")    

@app.route("/logout",methods=["POST","GET"])
def logout():
    # response = make_response(render_template("login.html"))
    response = redirect("/login")
    response.delete_cookie("username")
    return response

if __name__ == "__main__":
    app.run(debug=True)