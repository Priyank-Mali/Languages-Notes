from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def home():
    time = datetime.now()
    # formate_time = time.strftime("%I:%H:%M:%S %p")
    formate_time = time.hour
    print(formate_time)

    if 5 <= formate_time < 12:
        greeting = "It's Morning" 
    
    elif 12 <= formate_time <= 16:
        greeting = "It's Afternoon"
    
    elif 16 < formate_time <= 20:
        greeting = "It's Evening"
    
    else:
        greeting = "It's Night"
         
    return "Hello," + greeting


if __name__ == "__main__":
    app.run(debug=True)