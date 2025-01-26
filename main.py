# Import necessary libraries
import streamlit as st
import plotly.express as px


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


# Function to generate dates and temperatures based on the number of forecast days
def get_data(days):
    dates = ["2022 - 25-10", "2022-26-10", "2022-27-10"]
    temperatures = [10, 11, 15]
    # Multiply each temperature by the number of days
    temperatures = [ days * i for i in temperatures]
    return dates, temperatures


# Get the dates and temperatures based on the selected number of days
d, t = get_data(days)

# Create a Plotly line chart with the dates and temperatures
figure = px.line(x=d, y=t, labels={"x": "Date", "y": " Temperature (C)"})
# Display the Plotly chart in the Streamlit app
st.plotly_chart(figure)