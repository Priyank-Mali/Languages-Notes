from flask import Flask

"""
Here, an instance of the Flask class is created, and the special variable __name__ is passed as an argument. This variable helps Flask determine the root path of the application.
"""
app = Flask(__name__)
# app = Flask("__main__")


"""
This line is a decorator that tells Flask which URL should trigger the associated function. In this case, "/" refers to the root URL (e.g., http://localhost:5000/).
"""
@app.route("/")
def helloworld():
    msg = "<h1>hello world from priyank mali</h1>"
    return msg

# @app.route("/<name>")
# def helloworld(name):
#     msg = f"<h1>hello world from {name} mali</h1>"
#     return msg

if __name__ == '__main__':
    # app.run(port=5001,debug=True)
    app.run(debug=True)
    # app.run(debug=False)

