import pandas as pd
import matplotlib.pyplot as plt

sp500 = pd.read_csv('sp500_data.csv')
sp500['MSFT'].plot()
plt.show()
