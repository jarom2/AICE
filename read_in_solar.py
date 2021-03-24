import pandas as pd
import plotly.graph_objects as go

solar_gen = pd.read_csv("new_processed_solar.csv")
fig = go.Figure(go.Scatter(x=solar_gen['TIME'], y=solar_gen['Solar_Power'], name='Solar Generation'))
fig.update_layout(title='Averaged Solar Generation', showlegend=True)
fig.write_image("avg_solar_gen.jpg")
