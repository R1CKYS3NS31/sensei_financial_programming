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

# 100 day moving average
apple['100ma'] = apple['Adj Close'].rolling(window=100, min_periods=0).mean()
# The rolling function stacks a specific amount of entries, in order to make a statistical calculation possible.
# The window parameter is the one which defines how many entries we are
# going to stack. But there is also the min_periods parameter. This one defines
# how many entries we need to have as a minimum in order to perform the
# calculation. This is relevant because the first entries of our data frame won’t
# have a hundred previous to them. By setting this value to zero we start the
# calculations already with the first number, even if there is not a single
# previous value. This has the effect that the first value will be just the first
# number, the second one will be the mean of the first two numbers and so on,
# until we get to a hundred values. By using the mean function, we are obviously calculating the arithmetic
# mean. However, we can use a bunch of other functions like max, min or
# median if we like to.
apple.dropna(inplace=True)
# We do this by using the dropna function. If we would have had any entries
# with NaN values in any column, they would now have been deleted.

# print(apple.head())

# visualization
ax1 = plt.subplot2grid((6,1), (0,0),rowspan=4,colspan=1)
ax2 = plt.subplot2grid((6,1), (4,0),rowspan=2,colspan=1,sharex=ax1)

ax1.plot(apple.index,apple['Adj Close'])
ax1.plot(apple.index,apple['100ma'])
ax2.fill_between(apple.index,apple['Volume'])
plt.tight_layout()
plt.show()