import pandas as pd
import plotly.graph_objects as go

solar_gen = pd.read_csv("new_processed_solar.csv")
weather_data = pd.read_csv("weather_data.csv")
combined_data = pd.read_csv("combined_data.csv")
print(solar_gen.shape)
print(weather_data.shape)
print(combined_data.shape)
