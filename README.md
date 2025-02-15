# Weather Forecast Data App
This is a Streamlit app that provides accurate 5-day weather forecasts for any location. Users can input a place, select the number of forecast days (1 to 5), and choose the type of data to view (Temperature or Sky conditions). The app fetches weather data from the OpenWeatherMap API and displays it in an interactive Plotly chart or as images representing sky conditions.

# Features
- **Input Field**: Enter the name of a place to get the weather forecast.
- **Slider**: Select the number of forecast days (1 to 5).
- **Dropdown Menu**: Choose to view either Temperature or Sky conditions.
- **Temperature Chart**: Displays a line chart of temperatures in Celsius.
- **Sky Conditions**: Displays images representing sky conditions (Clear, Clouds, Rain, Snow).
- **Error Handling**: Provides user-friendly error messages for invalid or misspelled place names.

# Setup Instructions

# Prerequisites
- Python 3.7 or higher
- `pip` (Python package installer)

# Installation
To run the app locally, follow these steps:

1. **Clone the repository**:
   ```sh
   git clone https://github.com/your-username/weather-forecast-data-app.git

2. Navigate to the Project Directory:
  cd weather-forecast-data-app

3. Create a virtual environment:
  python -m venv venv

4. Activate the virtual environment:
   venv\Scripts\activate
   
5. Install the required dependencies:
   pip install -r requirements.txt

6. Add your OpenWeatherMap API key:
   Create a .env file in the root directory of the project and add your OpenWeatherMap API key
   API_KEY=your_openweathermap_api_key

# Running the App
  Run the Streamlit app:
  streamlit run [main.py](http://_vscodecontentref_/2)

# Open your web browser:
 The app will be available at http://localhost:8501.

# Important Components
  main.py: The main Streamlit app file that integrates the user interface and displays the weather data.
  backend.py: Handles API calls to OpenWeatherMap and processes the weather data.
  images/: Contains images representing different sky conditions (Clear, Clouds, Rain, Snow).

# API Integration
  The app uses the OpenWeatherMap API to fetch weather data. Make sure to sign up for an API key and add it to your .env file as shown in the installation steps.
  images/: Contains images representing different sky conditions (Clear, Clouds, Rain, Snow).
