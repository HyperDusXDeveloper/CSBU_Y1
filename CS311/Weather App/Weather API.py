from flask import Flask, jsonify
from weather_fetcher import WeatherFetcher  # Assuming the previous code is saved as weather_fetcher.py

app = Flask(__name__)

# Replace with your actual OpenWeatherMap API key (ideally, use environment variables)
API_KEY = "YOUR_OPENWEATHERMAP_API_KEY"
weather_fetcher = WeatherFetcher(API_KEY)

@app.route('/weather/<city>', methods=['GET'])
def get_weather_api(city):
    weather_data = weather_fetcher.get_current_weather(city)
    if weather_data:
        return jsonify(weather_data)
    else:
        return jsonify({"error": "City not found or weather data unavailable"}), 404

@app.route('/forecast/<city>', methods=['GET'])
def get_forecast_api(city):
    forecast_data = weather_fetcher.get_forecast(city)
    if forecast_data:
        return jsonify(forecast_data)
    else:
        return jsonify({"error": "City not found or forecast data unavailable"}), 404

if __name__ == '__main__':
    app.run(debug=True)