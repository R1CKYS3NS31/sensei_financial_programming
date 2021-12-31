import pandas as pd
import matplotlib.pyplot as plt

sp500 = pd.read_csv('sp500_data.csv')
correlation =  sp500.corr()
print(correlation)
plt.matshow(correlation)
plt.show()
