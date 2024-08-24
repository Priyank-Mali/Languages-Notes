from flask import Flask

app = Flask("__main__")

@app.route("/home")
@app.route("/home/<username>")
def home(username="Guest"):
    return "<h1>This is home view, Hello, </h1>" + username

# @app.route("/home/")
# def home():
#     return "<h1>This is home view</h1>"

@app.route("/about")
def about():
    return "<h1>This is about view</h1>"

def contact():
    return "<h1>This is contact view</h1>"

# @app.route("/blog/<int:blog_no>")
@app.route("/blog/<blog_no>")
def blog(blog_no):
    return "<h1>The Blog Number is: " + blog_no 
    # return "<h1>The Blog Number is: " + str(blog_no) 

@app.route("/check_number/<int:number>")
def check_num(number):
    if number % 2 == 0:
        return f"<h1>The {number} is Even."
    else:
        return f"<h1>The {number} is Odd."

app.add_url_rule("/contact","contact",contact)
if __name__ == "__main__":
    app.run(debug=True)