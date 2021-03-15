import pandas as pd
import plotly.graph_objects as go

solar_gen = pd.read_csv("weather_data.csv")

fig = go.Figure(go.Scatter(x=solar_gen['date_time'], y=solar_gen['rso'], name='Solar Radiation'))
fig.update_layout(title='Solar Radiation', showlegend=True)
fig.write_image("fig2.jpg")
