import os
import requests
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Your API key for accessing the OpenWeatherMap API
API_KEY = os.getenv("API_KEY")  # Ensure this matches the key in your .env file

# Function to get weather data for a specific place
def get_data(place, forecast_days=None):
    # Construct the URL for the API request
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"
    
    # Make the HTTP request to the API
    response = requests.get(url)
    
    # Parse the JSON response into a Python dictionary
    data = response.json()
    
    # Extract the list of forecast data
    filtered_data = data["list"]

    # Calculate the number of data points to keep based on the number of forecast days
    nr_values = 8 * forecast_days  # 8 data points per day
    
    # This slice will keep the first nr_values data points from the filtered_data list.
    filtered_data = filtered_data[:nr_values]
    
    # Return the filtered data
    return filtered_data


# Main block to test the function
if __name__ == "__main__":
    # Print the temperature data for Tokyo for the next 3 days
    print(get_data(place="Tokyo", forecast_days=3))
