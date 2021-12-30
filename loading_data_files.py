from pandas_datareader import data as web
import pandas as pd
import datetime as dt

start = dt.date(2017, 1, 1)
# end  = dt.datetime(2019, 1, 1)
end = dt.datetime.now()

# df = pd.read_csv('./apple.csv')
# df=pd.read_excel('./apple.xlsx')
# df= pd.read_html('./apple.html')
df= pd.read_json('./apple.json')
print(df)