import requests
import json
from datetime import datetime

class WeatherFetcher:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "http://api.openweathermap.org/data/2.5/weather?"
        self.forecast_url = "http://api.openweathermap.org/data/2.5/forecast?"

    def _get_weather_data(self, url):
        try:
            response = requests.get(url)
            response.raise_for_status()  # Raise an exception for bad status codes
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error fetching data: {e}")
            return None

    def get_current_weather(self, city):
        complete_url = self.base_url + "appid=" + self.api_key + "&q=" + city + "&units=metric&lang=en"
        weather_data = self._get_weather_data(complete_url)
        return self._process_current_weather(weather_data)

    def get_forecast(self, city):
        complete_url = self.forecast_url + "appid=" + self.api_key + "&q=" + city + "&units=metric&lang=en"
        forecast_data = self._get_weather_data(complete_url)
        return self._process_forecast(forecast_data)

    def _process_current_weather(self, data):
        if data and data["cod"] == 200:
            return {
                "city": data["name"],
                "country": data["sys"]["country"],
                "latitude": data["coord"]["lat"],
                "longitude": data["coord"]["lon"],
                "temperature": data["main"]["temp"],
                "feels_like": data["main"]["feels_like"],
                "humidity": data["main"]["humidity"],
                "pressure": data["main"]["pressure"],
                "wind_speed": data["wind"].get("speed"),
                "wind_direction": data["wind"].get("deg"),
                "description": data["weather"][0]["description"],
                "icon": data["weather"][0]["icon"],
                "timestamp": datetime.utcfromtimestamp(data["dt"]).strftime('%Y-%m-%d %H:%M:%S UTC')
            }
        return None

    def _process_forecast(self, data):
        if data and data["cod"] == "200":
            forecast_list = []
            for item in data["list"]:
                forecast_list.append({
                    "timestamp": datetime.utcfromtimestamp(item["dt"]).strftime('%Y-%m-%d %H:%M:%S UTC'),
                    "temperature": item["main"]["temp"],
                    "feels_like": item["main"]["feels_like"],
                    "humidity": item["main"]["humidity"],
                    "pressure": item["main"]["pressure"],
                    "wind_speed": item["wind"].get("speed"),
                    "wind_direction": item["wind"].get("deg"),
                    "description": item["weather"][0]["description"],
                    "icon": item["weather"][0]["icon"]
                })
            return {
                "city": data["city"]["name"],
                "country": data["city"]["country"],
                "forecast": forecast_list
            }
        return None

if __name__ == "__main__":
    # Replace with your actual OpenWeatherMap API key
    api_key = "YOUR_OPENWEATHERMAP_API_KEY"
    weather_fetcher = WeatherFetcher(api_key)

    city_name = input("Enter city name: ")
    current_weather = weather_fetcher.get_current_weather(city_name)

    if current_weather:
        print("\nCurrent Weather:")
        for key, value in current_weather.items():
            print(f"{key.capitalize()}: {value}")
    else:
        print("Could not retrieve current weather data.")

    forecast = weather_fetcher.get_forecast(city_name)
    if forecast:
        print("\nWeather Forecast:")
        for item in forecast["forecast"][:5]: # Displaying the first 5 forecasts
            print(f"Timestamp: {item['timestamp']}")
            print(f"Temperature: {item['temperature']} °C")
            print(f"Description: {item['description']}")
            print(f"Icon: {item['icon']}")
            print("-" * 20)
    else:
        print("Could not retrieve forecast data.")