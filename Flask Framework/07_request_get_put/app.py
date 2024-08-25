from flask import Flask,request
from flask.templating import render_template

app = Flask(__name__)

@app.route("/")
def home():
    # print(request.__dict__)
    # print(request.args)
    # print(request.query_string)
    # return "okay"

    return render_template("query_string.html")

@app.route("/mydata",methods=["POST"])    
def my_data():
    name_ = request.form.get('name')
    phone_ = request.form['phone']
    print(name_,phone_)
    return "My name is {} and phone number is {}".format(name_,phone_)

@app.route("/data")
def take_data():
    """
    if method is "GET" : 
    request.args.get("name")
    request.args["phone"]
    """

    """
    if method is "POST" :
    
    request.form.get("name")
    request.form["phone"]
    """
    
    name_ = request.args.get("name")
    phone_ = request.args.get("phone")
    print(name_,phone_)
    return render_template("data.html")

if __name__ == "__main__":
    app.run(debug=True)