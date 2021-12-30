from pandas_datareader import data as web
import pandas as pd
import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style

style.use('ggplot')
start = dt.date(2017, 1, 1)
# end  = dt.datetime(2019, 1, 1)
end = dt.datetime.now()

df= pd.read_json('./apple.json')
# print(df)

df['Adj Close'].plot()
# Since the date is the index of our data frame, Matplotlib uses it for the x-axis. The y-values are then our adjusted close
# values.
# For different matplotlib plotting style: https://bit.ly/2OSCTdm


plt.xlabel('Date')
plt.ylabel('Adjusted Close')
plt.title('AAPL Share Price')

plt.show()
