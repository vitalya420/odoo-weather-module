import os

import requests


class WeatherAPI:
	def __init__(self, api_key: str = None):
		"""
		Weather api.

		I have used the openweathermap.org API.
		The API key can be passed as a parameter or inserted into the OPENWEATHERMAP_API_KEY environment variable.
		If the environment variable is set and an argument is passed, the key from the environment will be used
		"""
		self.api_key = os.environ.get('OPENWEATHERMAP_API_KEY', api_key)
		assert self.api_key is not None, "Openweathermap api key required. Get it here: " \
										 "https://home.openweathermap.org/api_keys "

	def get_weather(self, city: str, **extra: dict) -> dict:
		"""
		Function that makes an http request to Openweathermap
		@param city: the city whose weather we want to get
		@param extra: additional arguments for requests.get (...). Documentation:
					  https://docs.python-requests.org/en/master/user/quickstart/
		@return: json response from API.
		"""
		res = requests.get(
			f"http://api.openweathermap.org/data/2.5/weather",
			params={
				"q": city,
				"appid": self.api_key
			},
			**extra
		)
		return res.json()

	@staticmethod
	def formatted(payload: dict) -> str:
		"""
		Get string representation of get_weather
		"""

		if payload['cod'] != 200:
			return "Unable to get weather"

		weather = payload['weather'][0]['description'].capitalize()  # General info
		temperature = payload['main']['temp'] - 273.15  # Convert temperature to Celsius
		return f"{weather}, {round(temperature, 2)} °C"
