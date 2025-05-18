from flask import Flask, render_template, request
import pandas as pd
import requests
import numpy as np
from joblib import load
import sklearn
import os
import warnings

app = Flask(__name__)

# Suppress version mismatch warnings
warnings.filterwarnings("ignore", category=UserWarning)

# API configuration
API_KEY = '8KYQAE79TA4NRE7CYNU9BC9G6'
API_URL = "https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/weatherdata/forecast?locations={lat}%2C{lon}&aggregateHours=24&unitGroup=us&shortColumnNames=false&contentType=json&key=" + API_KEY

def load_resources():
    """Load all required resources with error handling"""
    resources = {}
    try:
        resources['model'] = load('flood_model.pkl')
        resources['scaler'] = load('flood_scaler.pkl')

        current_version = sklearn.__version__
        print(f"Current scikit-learn version: {current_version}")

        encodings = ['utf-8', 'latin1', 'iso-8859-1', 'cp1252', 'utf-16']
        for encoding in encodings:
            try:
                resources['cities_df'] = pd.read_csv('cities.csv', encoding=encoding)
                print(f"Successfully loaded cities.csv with {encoding} encoding")
                break
            except UnicodeDecodeError:
                continue
        else:
            raise ValueError("Failed to read cities.csv with any supported encoding")
        
        return resources

    except Exception as e:
        print(f"Error loading resources: {str(e)}")
        raise

# Load resources at startup
try:
    resources = load_resources()
    model = resources['model']
    scaler = resources['scaler']
    cities_df = resources['cities_df']
except Exception as e:
    print(f"Critical error during startup: {str(e)}")
    exit(1)

@app.route('/plots')
def plots():
    return render_template('plots.html')

@app.route('/heatmaps')
def heatmaps():
    return render_template('heatmaps.html')

@app.route('/satellite')
def satellite():
    return render_template('satellite.html')


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        try:
            city = request.form.get('city', '').strip()
            if not city:
                return render_template('predicts.html', error="Please enter a city name")
            
            # Find city coordinates
            city_row = cities_df[cities_df['City'].str.lower() == city.lower()]
            if city_row.empty:
                return render_template('predicts.html', error="City not found in our database")

            lat = city_row.iloc[0]['lat']
            lon = city_row.iloc[0]['lng']

            # Fetch weather data
            response = requests.get(API_URL.format(lat=lat, lon=lon))
            if response.status_code != 200:
                return render_template('predicts.html', error="Weather API Error")

            data = response.json()
            location_key = list(data['locations'].keys())[0]
            values = data['locations'][location_key]['values'][0]

            # Extract features
            temp = values.get('temp', 0)
            max_temp = values.get('maxt', temp)
            wind_speed = values.get('wspd', 0)
            cloudcover = values.get('cloudcover', 0)
            precip = values.get('precip', 0)
            humidity = values.get('humidity', 0)

            # Prepare and predict
            input_features = np.array([[temp, max_temp, wind_speed, cloudcover, precip, humidity]])
            scaled_features = scaler.transform(input_features)

            prediction_proba = model.predict_proba(scaled_features)[0][1]
            prediction = model.predict(scaled_features)[0]

            flood_status = 'Flood Risk' if prediction == 1 else 'No Flood Risk'
            risk_percentage = round(prediction_proba * 100, 2)

            return render_template('predicts.html', 
                                    result=True,
                                    city=city.title(),
                                    temp=temp,
                                    max_temp=max_temp,
                                    wind_speed=wind_speed,
                                    cloudcover=cloudcover,
                                    precip=precip,
                                    humidity=humidity,
                                    flood_status=flood_status,
                                    risk_percentage=risk_percentage)

        except Exception as e:
            print(f"Unexpected error: {str(e)}")
            return render_template('predicts.html', error="An unexpected error occurred")
    
    return render_template('predicts.html')

if __name__ == '__main__':
    app.run(debug=True)
