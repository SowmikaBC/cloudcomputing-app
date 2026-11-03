
from flask import Flask, jsonify
from datetime import datetime
from zoneinfo import ZoneInfo

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome! Current Date and Time Application is Running."

@app.route('/getcurrentdateandtime')
def get_current_date_and_time():

    current_time = datetime.now(ZoneInfo("Asia/Kolkata"))

    return jsonify({
        "date": current_time.strftime("%d-%m-%Y"),
        "time": current_time.strftime("%I:%M:%S %p"),
        "day": current_time.strftime("%A"),
        "timezone": "Asia/Kolkata"
    })

if __name__ == '__main__':
    app.run()
