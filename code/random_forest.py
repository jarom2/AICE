import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.ensemble import RandomForestRegressor

data = pd.read_csv('../data/cnn_combined_data.csv')
y = data['Solar_Power']
data.drop('Solar_Power', 1, inplace=True)
x = data.to_numpy()
y = y.to_numpy()
x = np.nan_to_num(x, copy=True)
y = np.nan_to_num(y, copy=True)
y = y/100

print(x.shape)
print(y.shape)

regressor = RandomForestRegressor(n_estimators=100, random_state=0)
regressor.fit(x, y)
predictions = regressor.predict(x)

title_name = "Actual vs Predicted Solar Generation (Random Forest)"
x_axis_label = "Real"
y_axis_label = "Predicted"

plt.scatter(y, predictions)
plt.savefig('../figures/rf_1.jpg')


