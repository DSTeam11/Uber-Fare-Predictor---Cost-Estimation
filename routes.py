from application import app
from flask import render_template, request
import numpy as np
import pickle

model = pickle.load(open('UberFarePredictor.pkl', 'rb'))

# Decorator to access the app
@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")

# Decorator to access the service
@app.route("/predict_fare", methods=['GET', 'POST'])

def predict_fare():
        # Retrieve data from the form
        month = int(request.form['month'])
        year = int(request.form['year'])
        date = int(request.form['date'])
        hour = int(request.form['hour'])
        minute = int(request.form['minute'])
        seconds = int(request.form['seconds'])
        pickup_longitude = float(request.form['pickup_longitude'])
        pickup_latitude = float(request.form['pickup_latitude'])
        dropoff_longitude = float(request.form['dropoff_longitude'])
        dropoff_latitude = float(request.form['dropoff_latitude'])

        array1 = np.array([month, year, date, hour, minute, seconds,
                          pickup_longitude, pickup_latitude,
                          dropoff_longitude, dropoff_latitude])
        pred = model.predict([array1])
        return render_template("index.html", data=pred)


