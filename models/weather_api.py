import requests
import json


class WeatherAPI():
	def __init__(self, api_key: str = "f3282f0584edbaeba2b364d2b954ac20"):
		self.api_key = api_key

	def get_weather(self, city: str, **extra: dict) -> dict:
		res = requests.get(
			f"http://api.openweathermap.org/data/2.5/weather",
			params = {
				"q": city,
				"appid": self.api_key
			},
			**extra
		)
		return res.json()

	@staticmethod
	def formatted(payload: dict) -> str:
		"""
		Get string representation of weather from dictionary
		"""
		if payload['cod'] != 200:
			return ""

		weather = payload['weather'][0]['description'].capitalize() # General info
		temperature = payload['main']['temp'] - 273.15 	# Convert temperature to Celsium
		return f"{weather}, {round(temperature, 2)} °C"
