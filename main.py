# Import necessary libraries
import streamlit as st
import plotly.express as px
from backend import get_data

# Add title, text imput, slider, and dropdown menu and subheader


st.title("Get Accurate 5-Day Weather Forecasts for Any Location")
# Input field for the user to enter a place
place = st.text_input("Place: ")
# Slider for the user to select the number of forecast days
days = st.slider("Forcast Days", min_value=1, max_value=5,
                 help="Select the number of forecasted days")
# Dropdown menu for the user to select the type of data to view
option = st.selectbox("Select data to view", ("Temperature", "Sky"))
# Display a subheader with the selected options
st.subheader(f"{option} for the next {days} days in {place}")

if place:
    try:
        # Get the data based on the selected place, forcast days, and data type
        filtered_data = get_data(place, days)

        if option == "Temperature":
            # Convert temperatures from Kelvin to Celsius
            temperatures = [dict["main"]["temp"] / 10 for dict in filtered_data]
            # Create a Plotly line chart with the dates and temperatures
            dates = [dict["dt_txt"] for dict in filtered_data]
            # Create a Plotly line chart with the dates and temperatures
            figure = px.line(x=dates, y=temperatures, labels={"x": "Date", "y": "Temperature (C)"})
            # Display the Plotly chart in the Streamlit app
            st.plotly_chart(figure)

        if option == "Sky":
            images = {
                "Clear": "images/clear.png",
                "Clouds": "images/cloud.png",
                "Rain": "images/rain.png",
                "Snow": "images/snow.png"
            }
            sky_conditions = [dict["weather"][0]["main"] for dict in filtered_data]
            images_path = [images[condition] for condition in sky_conditions]
            print(sky_conditions)
            st.image(images_path, width=115)

    except KeyError:
        st.write("The place you entered could not be found. Please try again.")
