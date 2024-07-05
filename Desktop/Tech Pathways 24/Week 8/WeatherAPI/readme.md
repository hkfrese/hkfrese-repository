Documentation
Endpoint Description
Endpoint: GET /weather
Description: Retrieves weather information for a specific city.
Query Parameter: city (string, required): Name of the city for which to retrieve weather information.
Response Format
Success (200 OK):
json

{
  "city_name": "City Name",
  "current_temperature": 22.5,
  "weather_condition": "Sunny",
  "humidity": 60,
  "wind_speed": 15.3
}
Error (400 Bad Request):
json

{
  "error": "City parameter is required"
}
Error (404 Not Found):
json

{
  "error": "City not found"
}
Error (500 Internal Server Error):
json

{
  "error": "An error occurred while fetching the weather data"
}

Instructions to Run the API Server

Install Flask and requests:
pip install Flask requests
Save the code to a file named app.py.
Run the server:
The API server will start on http://127.0.0.1:5000

Testing the API
Test the API endpoint using cURL:

curl -X GET "http://127.0.0.1:5000/weather?city=SanDiego"

Getting Your API

Go to WeatherAPI.com.
Sign up for a free account.
Log in and navigate to the API key section on the dashboard.
Copy your API key and replace 'YOUR_API_KEY' in the weatherapi.py file with your actual API key.