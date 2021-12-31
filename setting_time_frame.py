import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import matplotlib.dates as mdates
import datetime as dt

# load from a file
apple = pd.read_csv('./apple.csv')
data = apple['Adj Close']
# print(apple)

rstart = dt.datetime(2018, 7, 1)
rend = dt.datetime(2019, 1, 1)

fit_data = data.reset_index()
pos1 = fit_data[fit_data.Date >= rstart].index[0]
pos2 = fit_data[fit_data.Date <= rend].index[-1]
fit_data = fit_data.iloc[pos1:pos2]

dates = fit_data.Date.map(mdates.date2num)
fit = np.polyfit(date, fit_data['Adj Close'], 1)
fit1d = np.poly1d(fit)

plt.grid()
plt.plot(data.index, data.values, 'b')
plt.plot(data.index, fit1d(x), 'r')
plt.show()
# ricky has bugs
