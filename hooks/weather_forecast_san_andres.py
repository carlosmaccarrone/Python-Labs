"""
Weather Forecast Fetcher for San Andrés, Buenos Aires.

This script retrieves the current weather description from the 
official Argentine Meteorological Service (SMN) API for San Andrés, 
Buenos Aires.

Author: Carlos Esteban Maccarrone -cem- 2018
"""

import requests
import json

def get_weather_forecast():
    url = 'https://ws.smn.gob.ar/map_items/weather'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        # Index 35 corresponds to San Andrés, Buenos Aires in the dataset
        print(data[35]['weather']['tempDesc'])
    else:
        print(f"Failed to retrieve data. Status code: {response.status_code}")

if __name__ == "__main__":
    get_weather_forecast()