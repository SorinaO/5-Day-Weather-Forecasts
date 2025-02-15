This Streamlit app provides accurate 5-day weather forecasts for any location. Users can input a place, select the number of forecast days (1 to 5), and choose the type of data to view (Temperature or Sky conditions). The app fetches weather data from the OpenWeatherMap API and displays it in an interactive Plotly chart or as images representing sky conditions.



Features

Input Field: Enter the name of a place to get the weather forecast.
Slider: Select the number of forecast days (1 to 5).
Dropdown Menu: Choose to view either Temperature or Sky conditions.
Temperature Chart: Displays a line chart of temperatures in Celsius.
Sky Conditions: Displays images representing sky conditions (Clear, Clouds, Rain, Snow).
Error Handling: Provides user-friendly error messages for invalid or misspelled place names.



Example Usage

Enter a Place: Type the name of a city or location.
Select Forecast Days: Use the slider to choose the number of days for the forecast.
Choose Data Type: Select either Temperature or Sky conditions from the dropdown menu.
View Results: The app displays the weather data in a Plotly chart or as images.
Code Snippet



Installation

To install and run the weather forecast app, follow these steps:

1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/weather-forcast-data-app.git
    ```

2. Navigate to the project directory:
    ```bash
    cd weather-forecast-data-app
    ```

3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Run the Streamlit app:
    ```bash
    streamlit run app.py
    ```

5. Open your web browser and go to `http://localhost:8501` to view the app.
