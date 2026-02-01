# Import necessary libraries
import requests
import pandas as pd

# Step 1: Define location coordinates (example: Miami, FL)
latitude = 25.7617
longitude = -80.1918

# Step 2: Construct the Open-Meteo API URL
# We'll request current weather data for the specified coordinates
url = f'https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current_weather=true'

# Step 3: Make a GET request to the API
# Note: verify=False disables SSL certificate verification (use only for testing/learning)
response = requests.get(url, verify=False)

# Step 4: Check if the request was successful and parse the data
if response.status_code == 200:
    data = response.json()

    # Step 5: Extract the 'current_weather' section
    weather_data = {
        'Latitude': latitude,
        'Longitude': longitude,
        'Temperature (C)': data['current_weather']['temperature'],
        'Wind Speed (km/h)': data['current_weather']['windspeed'],
        'Wind Direction (°)': data['current_weather']['winddirection'],
        'Weather Code': data['current_weather']['weathercode'],
        'Time': data['current_weather']['time']
    }

    # Step 6: Convert the data into a DataFrame
    df_weather = pd.DataFrame([weather_data])

    # Step 7: Display the DataFrame
    print(df_weather)
else:
    print(f"Failed to fetch weather data. Status code: {response.status_code}")