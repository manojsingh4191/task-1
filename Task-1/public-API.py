import requests
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Function to fetch weather data
def fetch_weather_data(city, api_key):
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric'  # To get temperature in Celsius
    }
    
    response = requests.get(base_url, params=params)
    data = response.json()
    
    if response.status_code == 200:
        return data
    else:
        print(f"Error fetching data: {data.get('message', 'Unknown error')}")
        return None

# Function to create a dashboard visualization
def create_visualization(weather_df):
    # Plotting temperature, humidity, and wind speed
    fig, axes = plt.subplots(1, 3, figsize=(18, 6))

    # Temperature
    sns.barplot(x='City', y='Temperature (°C)', data=weather_df, ax=axes[0])
    axes[0].set_title('Temperature (°C)')

    # Humidity
    sns.barplot(x='City', y='Humidity (%)', data=weather_df, ax=axes[1])
    axes[1].set_title('Humidity (%)')

    # Wind Speed
    sns.barplot(x='City', y='Wind Speed (m/s)', data=weather_df, ax=axes[2])
    axes[2].set_title('Wind Speed (m/s)')

    # Adjust layout
    plt.tight_layout()
    plt.show()

# Replace with your OpenWeatherMap API key
api_key = 'YOUR_API_KEY'

# Example: Fetch data for London
city = 'London'
weather_data = fetch_weather_data(city, api_key)

if weather_data:
    # Extract relevant data
    weather_info = {
        'City': weather_data['name'],
        'Temperature (°C)': weather_data['main']['temp'],
        'Humidity (%)': weather_data['main']['humidity'],
        'Pressure (hPa)': weather_data['main']['pressure'],
        'Wind Speed (m/s)': weather_data['wind']['speed'],
        'Weather': weather_data['weather'][0]['description'],
        'Weather Icon': weather_data['weather'][0]['icon']
    }

    # Convert to DataFrame for easier manipulation
    weather_df = pd.DataFrame([weather_info])

    # Create the visualization
    create_visualization(weather_df)
