import pandas as pd
import plotly.graph_objects as go

solar_gen = pd.read_csv("solar_generation.csv")

fig = go.Figure(go.Scatter(x=solar_gen['TIME'], y=solar_gen['Meter_value'], name='Solar Generation'))
fig.update_layout(title='Solar Generation', showlegend=True)
fig.write_image("fig1.jpg")
