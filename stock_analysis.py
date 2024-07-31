""" import pandas as pd
import pandas_datareader.data as web
import datetime

start = datetime.datetime(2022, 1, 1)
end = datetime.datetime(2022, 12, 31)

stock_data = web.DataReader('GOOGL', 'yahoo', start, end)
print(stock_data['Close'])
 """

import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# Replace 'EG1T.TL' with the correct ticker symbol for Enefit Green if necessary
ticker = 'EGR1T.TL'

# Fetch historical market data
stock_data = yf.download(ticker, start="2022-01-01", end="2024-07-30")

# Display the first few rows of the data
print(stock_data.head())

# Plot the closing prices
plt.figure(figsize=(10, 6))
plt.plot(stock_data['Close'], label='Close Price')
plt.title('Enefit Green Closing Prices')
plt.xlabel('Date')
plt.ylabel('Closing Price')
plt.legend()
plt.show()

# Perform a simple moving average (SMA) analysis
stock_data['SMA50'] = stock_data['Close'].rolling(window=50).mean()
stock_data['SMA200'] = stock_data['Close'].rolling(window=200).mean()

# Plot the closing prices along with the SMAs
plt.figure(figsize=(10, 6))
plt.plot(stock_data['Close'], label='Close Price')
plt.plot(stock_data['SMA50'], label='50-Day SMA')
plt.plot(stock_data['SMA200'], label='200-Day SMA')
plt.title('Enefit Green Closing Prices with SMAs')
plt.xlabel('Date')
plt.ylabel('Price')
plt.legend()
plt.show()

