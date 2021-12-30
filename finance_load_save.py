from pandas_datareader import data as web
# This module will be used to get our data from the Yahoo Finance
# API.
import datetime as dt

start = dt.date(2017, 1, 1)
# end  = dt.datetime(2019, 1, 1)
end = dt.datetime.now()

df= web.DataReader('AAPL','yahoo',start,end)
print(df)
# Open: That’s the share price the stock had when the markets opened that day.
# Close: That’s the share price the stock had when the markets closed that day.
# High: That’s the highest share price that the stock had that day.
# Low: That’s the lowest share price that the stock had that day.
# Volume: Amount of shares that changed hands that day.
# Adj. Close: The adjusted close value that takes things like stock splits into consideration.
# print(df['Close'])

# save the data
# csv
# df.to_csv('apple.csv',sep=';')
df.to_csv('apple.csv')
# excel
df.to_excel('apple.xlsx')
# html
df.to_html('apple.html')
# json
df.to_json('apple.json')