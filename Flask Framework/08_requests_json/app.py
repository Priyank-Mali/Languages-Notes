from flask import Flask,request
import requests

app = Flask(__name__)

@app.route('/makejson')
def make_json():
    person = {
        "name" : "priyank",
        "language" : "python",
        "framework" : ["Flask" , "Djano" , "Bottle"]
    }
    url = "http://127.0.0.1:5000/getjson"
    response = requests.post(url,json=person)
    return response.text

@app.route("/getjson",methods=["POST","GET"])
def get_json():
    if request.is_json:
        # jsondata = request.get_json()
        jsondata = request.json
        return "Json Data : {}".format(jsondata) 
    else:
        return "Not Json" 

if __name__ == "__main__":
    app.run(debug=True)