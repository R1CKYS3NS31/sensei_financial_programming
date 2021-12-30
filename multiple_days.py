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


# load from a file
apple = pd.read_csv('./apple2019.csv')
facebook = pd.read_csv('./facebook2019.csv')
amazon = pd.read_csv('./amazon2019.json')

apple_ohlc = apple['Adj Close'].resample('10D').ohlc()
apple_ohlc.reset_index(inplace=True)
apple_ohlc['Date']= apple_ohlc['Date'].map(mdates.date2num)
# print(apple_ohlc)
# we take ten days (10D). At the end we apply the ohlc function, to
# get the four values out of our entries. Then we again have to convert our date
# into a numerical format.

apple_volume = apple['Volume'].resample('10D').sum()

ax1= plt.subplot2grid((6,1), (0,0),rowspan=4,colspan=1)
ax2 = plt.subplot2grid((6,1), (4,0),rowspan=2,colspan=1,sharex=ax1)

ax1.xaxis_date()
candlestick_ohlc(ax1,apple_ohlc.values, width=5,colorup='g',colordown='r')
ax2.fill_between(apple_volume.index.map(mdates.date2num),apple_volume.values)
plt.tight_layout()
plt.show()
# ricky has bugs

