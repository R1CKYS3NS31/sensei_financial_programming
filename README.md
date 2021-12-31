# Financial Programming

#### Modules to install
· Pandas
· Pandas-Datareader
· Matplotlib
· MPL-Finance
· NumPy
· Scikit-Learn
· Beautifulsoup4

pip install pandas
pip install pandas-datareader
pip install matplotlib
pip install mpl-finance
pip install scikit-learn
pip install beautifulsoup4

The Pandas-Datareader is an additional library which we are going to use, in order to load financial data from the internet. It loads data from APIs into data frames.

MPL-Finance is a library that works together with Matplotlib and allows us to
use special visualization for finance. We will use it for plotting candlestick
charts.

beautifulsoup4 - powerful web scraping library. We are going to use it in order to extract financial data out of HTML files.

#### Webscraping

With webscraping we are reading the HTML files of a website, in order to extract some specific information we are looking for. In this case, we are going to use the Wikipedia page of the list of S&P 500 companies to get the information we need. 
Link: https://en.wikipedia.org/wiki/List_of_S%26P_500_companies