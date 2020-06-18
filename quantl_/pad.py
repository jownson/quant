import pandas as pd
import quandl

quandl.ApiConfig.api_key = 'dfs3NNy17Yb9Adu9xfCC'
# quandl.ApiConfig.api_version = '2015-04-09'

# df = quandl.get('NSE/OIL')
# df = quandl.get_table('ZACKS/FC', ticker='AAPL')
# df = quandl.get('EOD/V')

df = quandl.get('EOD/AAPL', start_date='2015-01-01', end_date='2020-01-01')
df.to_csv('AAP0L.csv')

# quandl.bulkdownload('EOD', filename='c:\\quandl\\EOD_DB.zip') 收费

# df = quandl.get('EOD/AAPL', trim_start='2001-01-01',
#                 trim_end='2010-01-01', collapse='annual',
#                 transformation='rdiff', rows=4, sort_order='desc')
# df.to_csv('AAPL.csv')

# tickers = ['EOD/AAPL', 'EOD/BA', 'EOD/ZTO']
# tickers = ['EOD/BA']
# for ticker in tickers:
#     df = quandl.get(tickers, trim_start = "2000-12-12", trim_end = "2020-2-28")
#     tickerNoMarket = ticker.replace('EOD/', '')
#     csvFileName = 'c:\\quandl\\' + tickerNoMarket + '.csv'
#     df.to_csv(csvFileName)

print(df.head())
