#http://127.0.0.1:5000/weather?city=San Diego, CA

from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

API_KEY = '03761ef0c96f4dc6a7c161345240507'
WEATHER_API_URL = 'http://api.weatherapi.com/v1/current.json'

@app.route('/weather', methods=['GET'])
def get_weather():
    city = 'San Diego, CA'
    response = requests.get(WEATHER_API_URL, params={'key': API_KEY, 'q': city})
    if response.status_code == 200:
        data = response.json()
        weather_info = {
            'city_name': data['location']['name'],
            'current_temperature': data['current']['temp_c'],
            'weather_condition': data['current']['condition']['text'],
            'humidity': data['current']['humidity'],
            'wind_speed': data['current']['wind_kph']
        }
        return jsonify(weather_info), 200
    elif response.status_code == 400:
        return jsonify({'error': 'City not found'}), 404
    else:
        return jsonify({'error': 'An error occurred while fetching the weather data'}), 500

if __name__ == '__main__':
    app.run(debug=True)
