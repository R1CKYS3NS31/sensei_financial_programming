import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import matplotlib.dates as mdates

# load from a file
apple = pd.read_json('./apple2019.json')
data = apple['Adj Close']
# print(apple)
x = data.index.map(mdates.date2num)
fit = np.polyfit(x, data.values, 1)
fit1d = np.poly1d(fit)
# You will notice that this implementation of linear regression is quite different
# from the one, we already used in the last volume with scikit-learn. Here we
# use NumPy. First we call the polyfit method to fit a model for the x-values
# (our dates) and the y-values (the prices). The last parameter (one) is the
# degree of the function. In this case, it is linear. What this function returns to
# us is a list of coefficients. To now use this list and make an actual function of
# it, we need the second method poly1d . It takes the list and constructs a
# function for x . So our variable fit1d is actually a callable function.

plt.grid()
plt.plot(data.index, data.values, 'b')
plt.plot(data.index, fit1d(x), 'r')
plt.show()
