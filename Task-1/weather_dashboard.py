import os # For accessing environment variables securely
import requests # For making HTTP requests to the OpenWeatherMap API
import pandas as pd # For data manipulation and analysis
import streamlit as st # For building the interactive web dashboard
import matplotlib.pyplot as plt # For creating visualizations
import seaborn as sns # For enhanced statistical visualizations
from dotenv import load_dotenv # For loading environment variables from a .env file

# ----------------------------------
# Load Environment Variables
# ----------------------------------
# Load secrets from the .env file to keep the API key secure and out of the source code.
load_dotenv()
API_KEY = os.getenv("OPENWEATHER_API_KEY")

# Define the base endpoints for OpenWeatherMap (Forecast vs Current weather)
BASE_FORECAST_URL = "https://api.openweathermap.org/data/2.5/forecast" # 5-day forecast endpoint (returns data in 3-hour intervals)
BASE_CURRENT_URL = "https://api.openweathermap.org/data/2.5/weather" # Current weather endpoint (returns a single snapshot of current conditions)


# ----------------------------------
# Fetch Current Weather
# ----------------------------------
def fetch_current_weather(city):
    """
    Fetches the current weather snapshot for a specific city.
    Returns the raw JSON response.
    """
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"  # We want Celsius, not Kelvin or Fahrenheit
    }

    # Make a GET request to the current weather endpoint with the specified parameters (city name, API key, and units)
    response = requests.get(BASE_CURRENT_URL, params=params) 

    # Parse the JSON response into a Python dictionary for easier access to weather data fields
    data = response.json()

    # Robust error handling: Check if the API returned a success code (200)
    if str(data.get("cod")) != "200":
        raise ValueError(data.get("message", "Error fetching current weather"))

    return data


# ----------------------------------
# Fetch Forecast Data
# ----------------------------------
def fetch_forecast(city):
    """
    Fetches the 5-day forecast.
    Note: The API returns data in 3-hour intervals.
    """
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    response = requests.get(BASE_FORECAST_URL, params=params)
    data = response.json()

    if str(data.get("cod")) != "200":
        raise ValueError(data.get("message", "Error fetching forecast"))

    return data


# ----------------------------------
# Convert Forecast to DataFrame
# ----------------------------------
def build_dataframe(data):
    """
    Parses the nested JSON response and converts it into a clean Pandas DataFrame
    for easier plotting and analysis.
    """
    records = [] # Initialize an empty list to store the extracted records from the forecast data

    # Loop through the forecast list and extract only the relevant metrics
    for entry in data["list"]: # list contains multiple forecast entries, each representing a 3-hour interval
        
        # For each entry, we extract the date_time, temperature, humidity, wind speed, and weather description, and store them in a dictionary format. This structured format allows us to easily convert it into a DataFrame later on.
        records.append({
            "date_time": entry["dt_txt"],
            "temperature": entry["main"]["temp"],
            "humidity": entry["main"]["humidity"],
            "wind_speed": entry["wind"]["speed"],
            "weather": entry["weather"][0]["description"]
        })

    # Convert the list of dictionaries into a Pandas DataFrame
    df = pd.DataFrame(records)
    
    # Convert string dates to datetime objects for proper time-series plotting
    df["date_time"] = pd.to_datetime(df["date_time"])

    # Sort the DataFrame by date_time to ensure that the time-series plots are in chronological order, which is crucial for accurate visualization of trends over time.
    df = df.sort_values("date_time")
    
    # Calculate a simple moving average (SMA) to smooth out temperature fluctuations
    # over 5 data points (approx 15 hours)
    df["rolling_avg"] = df["temperature"].rolling(5).mean()

    return df


# ----------------------------------
# Streamlit UI
# ----------------------------------
# Configure the page layout to 'wide' to accommodate the dashboard grids
st.set_page_config(page_title="Weather Dashboard", layout="wide") 
st.title("🌦 Weather Dashboard (Matplotlib + Seaborn)")

# Stop execution immediately if the API key is missing to prevent crash errors
if not API_KEY:
    st.error("API key not found. Please set it in .env file.")
    st.stop()

# User input for city name with a default value of "Mumbai"
city = st.text_input("Enter City Name", "Pune")

# Button to trigger data fetching and visualization 
if st.button("Get Weather Data"):

    try:
        # 1. Fetch and Process Data
        current = fetch_current_weather(city) # Get the current weather snapshot for the specified city
        forecast = fetch_forecast(city) # Get the 5-day forecast data (in 3-hour intervals)
        df = build_dataframe(forecast) # Convert the raw forecast data into a structured DataFrame for analysis and visualization

        # 2. Display Key Metrics (KPIs) at the top
        col1, col2, col3 = st.columns(3) # Create three columns to display the key metrics side by side
        col1.metric("🌡 Temperature", f"{current['main']['temp']} °C") 
        col2.metric("💧 Humidity", f"{current['main']['humidity']} %") 
        col3.metric("🌬 Wind Speed", f"{current['wind']['speed']} m/s")

        st.subheader("Current Condition")
        st.write(current["weather"][0]["description"].title()) # Display the current weather condition in a human-readable format (e.g., "Clear Sky", "Light Rain")

        # 3. Visualization Setup
        sns.set_style("darkgrid") # Sets a clean background for charts

        # Create a 2x2 grid of subplots for the dashboard view
        fig, axes = plt.subplots(2, 2, figsize=(14, 8)) # Larger figure size to accommodate multiple charts without clutter
        fig.suptitle(f"5-Day Forecast - {city}", fontsize=16) # Overall title for the dashboard to indicate the city and forecast period

        # Chart 1: Temperature vs Rolling Average
        # The solid line represents the actual temperature values over time, showing how the temperature fluctuates throughout the forecast period.
        sns.lineplot(
            ax=axes[0, 0], # Plot the temperature trend on the first subplot (top-left) 
            x="date_time", 
            y="temperature", 
            data=df, # DataFrame containing the forecast data, which includes the date_time and temperature columns
            label="Temperature"
        )

        # The dashed line represents the rolling average (SMA) of temperature.
        sns.lineplot(
            ax=axes[0, 0], # Plot the rolling average on the same subplot to compare it with the actual temperature trend
            x="date_time", 
            y="rolling_avg", 
            data=df,
            linestyle="--",
            label="Rolling Avg" 
        )
        axes[0, 0].set_title("Temperature Trend")
        axes[0, 0].tick_params(axis="x", rotation=45) # Rotate x-axis labels for better readability, especially when there are many time points close together

        # Chart 2: Humidity over time
        # The line plot shows how humidity levels change over the forecast period, allowing users to identify patterns such as increasing or decreasing humidity trends, which can be important for understanding weather conditions and potential discomfort levels.
        sns.lineplot(
            ax=axes[0, 1], # Plot the humidity trend on the second subplot (top-right)
            x="date_time",
            y="humidity",
            data=df
        )
        axes[0, 1].set_title("Humidity Trend")
        axes[0, 1].tick_params(axis="x", rotation=45)

        # Chart 3: Wind Speed over time
        # The line plot illustrates how wind speed varies throughout the forecast period, which can help users anticipate windy conditions or calm periods. This information is particularly useful for outdoor activities, travel planning, and understanding potential weather hazards.
        sns.lineplot(
            ax=axes[1, 0], # Plot the wind speed trend on the third subplot (bottom-left)
            x="date_time",
            y="wind_speed",
            data=df
        )
        axes[1, 0].set_title("Wind Speed Trend")
        axes[1, 0].tick_params(axis="x", rotation=45)

        # Chart 4: Bar chart of most frequent weather conditions
        # The bar chart displays the top 5 most common weather conditions in the forecast period, providing a quick visual summary of the predominant weather types (e.g., clear, cloudy, rain) that users can expect. This helps users understand the overall weather pattern and prepare accordingly.
        condition_counts = df["weather"].value_counts().head(5) # Get the top 5 most frequent weather conditions from the DataFrame
        sns.barplot(
            ax=axes[1, 1],
            x=condition_counts.values,
            y=condition_counts.index
        )
        axes[1, 1].set_title("Top Weather Conditions")

        # Adjust layout to prevent labels from overlapping
        plt.tight_layout()
        st.pyplot(fig)

    # Robust error handling to catch and display any issues that arise during data fetching or processing, such as network errors, invalid city names, or API issues. This ensures that users receive clear feedback on what went wrong instead of the app crashing.
    except Exception as e:
        st.error(f"Error: {e}")