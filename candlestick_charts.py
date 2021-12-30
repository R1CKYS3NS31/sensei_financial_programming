from mpl_finance import candlestick_ohlc
import matplotlib.dates as mdates
from matplotlib import style
import pandas as pd
import matplotlib.pyplot as plt
from pandas_datareader import data as web
import datetime as dt

style.use('ggplot')
# start = dt.datetime(2017, 1, 1)
# end = dt.datetime(2019, 1, 1)

# apple=web.DataReader('AAPL','yahoo',start,end)
# facebook = web.DataReader('FB','yahoo',start,end)
# amazon = web.DataReader('AMZN','yahoo',start,end)

# # save to a file
# apple.to_csv('apple2019.csv')
# facebook.to_csv('facebook2019.csv')
# amazon.to_csv('amazon2019.csv')


# load from a file
apple = pd.read_csv('./apple2019.csv')
facebook = pd.read_csv('./facebook2019.csv')
amazon = pd.read_csv('./amazon2019.json')

apple = apple[['Date','Open','High','Low','Low','Close']]
# Now, we have our columns in the right order but there is still a problem. Our
# date doesn’t have the right format and since it is the index, we cannot
# manipulate it. Therefore, we need to reset the index and then convert our
# datetime to a number.

# apple.reset_index(inplace=True)

# print(apple['Date'])
apple['Date'] = apple['Date'].map(mdates.date2num)
# print(apple)
# Now, we have our columns in the right order but there is still a problem. Our
# date doesn’t have the right format and since it is the index, we cannot
# manipulate it. Therefore, we need to reset the index and then convert our
# datetime to a number.

ax = plt.subplot()
candlestick_ohlc(ax, apple.values, width=5, colordown='r', colorup='g')
ax.grid()
ax.xaxis_date()
plt.show()
# ricky has bugs