import requests  # Send HTTP requests
from bs4 import BeautifulSoup
import json  # Convert Extrscting Result Into json File

# Prompt the user to enter a location
location = input("Enter a location (city name): ")
code =input("Enter the code (country code): ")

url = f"https://www.wunderground.com/weather/{code}/{location}"
response = requests.get(url)
response.raise_for_status()

soup = BeautifulSoup(response.text, 'html.parser')

  # Extract weather information
temperature_fahrenheit = soup.find(class_="wu-value wu-value-to").text.strip()
humidity = soup.find(class_="wu-value wu-value-to").text.strip()
wind_speed = soup.find(class_="wu-value wu-value-to").text.strip()
weather_conditions = soup.find(class_="condition-icon small-6 medium-12 columns").text.strip()

temperature_celsius = (float(temperature_fahrenheit) - 32) * 5 / 9

  # Store the data in a dictionary

weather_data = {
    'location': location,
    'temperature': temperature_celsius,
    'humidity': humidity,
    'wind_speed': wind_speed,
    'weather_conditions': weather_conditions
  }

  # Save the data to a JSON file
with open('weather_data.json', 'w') as file:
    json.dump(weather_data, file, indent=4)

  # Display the extracted information
print(f"Location: {location}")
print(f"Temperature: {temperature_celsius}")
print(f"Humidity: {humidity}")
print(f"Wind Speed: {wind_speed}")
print(f"Weather Conditions: {weather_conditions}")