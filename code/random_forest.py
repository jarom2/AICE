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
y = y/1000

x_train = x[0:4999]
x_test = x[5000:-1]

y_train = y[0:4999]
y_test = y[5000:-1]

print(y_test.shape)

with np.errstate(invalid='ignore'):

    # TRAIN DATA
    regressor = RandomForestRegressor(n_estimators=100, random_state=0)
    regressor.fit(x_train, y_train)
    predictions = regressor.predict(x_train)
    correlation = np.corrcoef(y_train, predictions)


    title_name = 'Actual vs Predicted Solar Generation (RF Training) Corr: {}'.format(correlation)
    x_axis_label = "Real (KW)"
    y_axis_label = "Predicted (KW)"

    plt.scatter(y_train, predictions)
    plt.title(title_name)
    plt.xlabel(x_axis_label)
    plt.ylabel(y_axis_label)
    plt.savefig('../figures/rf_train1.jpg')

    # TEST DATA
    predictions2 = regressor.predict(x_test)
    correlation2 = np.corrcoef(y_test, predictions2)

    title_name2 = "Actual vs Predicted Solar Generation (RF Test) Corr: {}".format(correlation2)
    x_axis_label2 = "Real (KW)"
    y_axis_label2 = "Predicted (KW)"

    plt.scatter(y_test, predictions2)
    plt.title(title_name2)
    plt.xlabel(x_axis_label2)
    plt.ylabel(y_axis_label2)
    plt.savefig('../figures/rf_test1.jpg')

