from flask import Flask, jsonify, request
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route('/api/weather', methods=['GET'])
def get_weather():
    city = request.args.get('city')
    api_key = '2681ad3b9fa5f33715c880dc8620b43d'
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
    
    response = requests.get(url)
    if response.status_code == 200:
        weather_data = response.json()
        return jsonify(weather_data)
    else:
        return jsonify({"error": "Unable to fetch weather data"})
    
@app.route('/api/cities', methods=['GET'])
def get_cities():
    keyword = request.args.get('keyword')
    api_key = '2681ad3b9fa5f33715c880dc8620b43d'
    url = f'http://api.openweathermap.org/geo/1.0/direct?q={keyword}&limit=5&appid={api_key}'
    
    response = requests.get(url)
    if response.status_code == 200:
        city_data = response.json()
        city_names = [city['name'] for city in city_data]
        return jsonify(city_names)
    else:
        return jsonify({"error": "Unable to fetch city data"})    

if __name__ == '__main__':
    app.run(debug=True)
