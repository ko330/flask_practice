from flask import Flask,request
import requests
import pandas as pd
import numpy as np
import io
from sklearn import linear_model
#dowload data
url = "https://raw.githubusercontent.com/nytimes/covid-19-data/master/us.csv"
download = requests.get(url).content
data = pd.read_csv(io.StringIO(download.decode('utf-8')))
data['date'] = pd.to_datetime(data['date'])
last_day = len(data)


actual_y=data['cases']
#collect last 30 days data & regression
TRAIN_X = np.arange(last_day-30,last_day)[:,np.newaxis]
TRAIN_Y = np.log(actual_y[last_day-30:last_day])
model = linear_model.LinearRegression()
model.fit(TRAIN_X,TRAIN_Y)
predict_x = np.arange(last_day-30, last_day)
predict_y = np.exp(model.predict(predict_x[:, np.newaxis]))

each_error = np.abs(actual_y[last_day-30:]-predict_y)/predict_y
threshold = max(each_error)*2


app = Flask(__name__)
@app.route('/api/data', methods=['POST'])
def anomaly_detection():
    entry=request.values.to_dict()
    date = entry['date']
    date = pd.to_datetime(date)
    input_x = (date - data['date'][0]).days  # convert date to int
    pred = np.exp(model.predict(np.array([input_x])[:, np.newaxis]))
    input_y = int(entry['cases'])
    diff = np.abs(input_y - pred) / pred
    if (diff) > threshold:
        requests.post('http://localhost:5001/api/alarm',data=entry)
        return "anomaly"
    else:
        return "normal"


app.run(port=5000)