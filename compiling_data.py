import pickle
import pandas as pd
import datetime as dt
from pandas_datareader import data as web

with open('sp500tickers.pickle','rb') as f:
    tickers = pickle.load(f)
main_df = pd.DataFrame()

print('Compiling data...')
for ticker in tickers:
    df = pd.read_csv('companies/{}.csv'.format(ticker))
    df.set_index('Date',inplace = True)
    df.rename(columns={'Adj Close':ticker},inplace=True)
    df.drop(['Open','High','Low','Close'],1,inplace= True)
    if main_df.empty:
        main_df = df
    else: main_df=main_df.join(df,how='outer')
main_df.to_csv('sp500_data.csv')
print('Data Compiled!')

