from flask import Flask

app = Flask(__name__)

@app.errorhandler(404)
def errorhandler(error):
    # return "You Enter Wrong Url"
    return error

@app.route("/login")
def login():
    return """
    <form>
        <lable for="name">Enter Your Name: </lable><br>
        <input type="text" name="name">
        <br>
        <input type="submit" value="submit">
    </form>
    """

if __name__ == "__main__":
    app.run(debug=True)