import bs4 as bs
import requests
import pickle
import os
import datetime as dt
import pandas_datareader as web


def load_sp500_tickers():
    link = 'https://en.wikipedia.org/wiki/List_of_S%26P_500_companies'
    response = requests.get(link)
    # We use the get function to make a HTTP request to the website and it returns
    # a response which we save into a variable. Now we need to create a soup object , in order to parse the content of the
    # response.
    soup = bs.BeautifulSoup(response.text, 'lxml')
    # The second parameter defines the parser that we choose. In this case, we pick lxml which is the
    # default choice.

    table = soup.find('table', {'class': 'wikitable sortable'})
    tickers = []
    for row in table.findAll('tr')[1:]:
        ticker = row.findAll('td')[0].text[:-1]
        tickers.append(ticker)
        return tickers

    # By using the findAll method we get all elements which are a table row. We
    # then select every element except for the first one, since it is the header. Then
    # we use the same function to get all the table data elements of the first column
    # (index zero). Notice that we are using the [:-1] notation here to cut of the last
    # two letters, since they contain a new line escape character. Finally, we save
    # our tickers into our array.
with open('sp500tickers.pickle', 'wb') as f:
    pickle.dump(tickers, f)

# loading share prices


def load_prices(reload_tickers=False):
    if reload_tickers:
        tickers = load_sp500_tickers()
    else:
        if os.path.exists('sp500tickers.pickle'):
            with open('sp500tickers', 'rb') as f:
                tickers = pickle.load(f)


if not os.path.exists('companies'):
    os.makedirs('companies')

start = dt.datetime(2016, 1, 1)
end = dt.datetime(2019, 1, 1)
for ticker in tickers:
    if not os.path.exists('companies/{}.csv'.format(ticker)):
        print('{} is loading...'.format(ticker))
        df = web.DataReader(ticker, 'yahoo', start, end)
        df.to_csv('companies/{}.csv'.format(ticker))
    else:
        print('{} already downloaded'.format(ticker))
# compiling data


def compile_data():
    with open('sp500tickers.pickle', 'rb') as f:
        tickers = pickle.load(f)
    main_df = pd.DataFrame()

    print('Compiling data...')
    for ticker in tickers:
        df = pd.read_csv('companies/{}.csv'.format(ticker))
        df.set_index('Date', inplace=True)
        df.rename(columns={'Adj Close': ticker}, inplace=True)
        df.drop(['Open', 'High', 'Low', 'Close'], 1, inplace=True)
        if main_df.empty:
            main_df = df
        else:
            main_df = main_df.join(df, how='outer')
main_df.to_csv('sp500_data.csv')
print('Data Compiled!')
load_prices(reload_tickers=True)
compile_data()
