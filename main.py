# Import necessary libraries
import streamlit as st
import plotly.express as px
from backend import get_data


st.title("Weather Forcast for The Next Days")
# Input field for the user to enter a place
place = st.text_input("Place: ")
# Slider for the user to select the number of forecast days
days = st.slider("Forcast Days", min_value=1, max_value=5,
                 help="Select the number of forecasted days")
# Dropdown menu for the user to select the type of data to view
option = st.selectbox("Select data to view", ("Temperature", "Sky"))
# Display a subheader with the selected options
st.subheader(f"{option} for the next {days} days in {place}")


# Get the data based on the selected place, forcast days, and data type
d, t = get_data(place, days, option)



# Create a Plotly line chart with the dates and temperatures
figure = px.line(x=d, y=t, labels={"x": "Date", "y": " Temperature (C)"})
# Display the Plotly chart in the Streamlit app
st.plotly_chart(figure)