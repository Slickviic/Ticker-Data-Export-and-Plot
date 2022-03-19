import numpy
import pandas as pd
import matplotlib as plt
import mplfinance as mpf
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
from datetime import datetime
import time
import yfinance as yf
import pandas_ta as pdta


#Get Ticker Data

ticker_name = "MSFT"

df = yf.Ticker(ticker_name).history(period="max", interval="1h", start = "2022-03-01")

#Calculate MACD/EMA values
macd = pdta.macd(close = df['Close'])
ema_30 = pdta.ema(close = df['Close'], length = 30)
ema_60 = pdta.ema(close = df['Close'], length = 60)
ema_365 = pdta.ema(close = df['Close'], length = 365)

#Append indicator values to Data Frame
df['MACD_12_26_9'] = macd['MACD_12_26_9']
df['EMA_30'] = ema_30
df['EMA_60'] = ema_60
df['EMA_365'] = ema_365

print(df)

#Create file path for ticker data export
file_path = f'C:/Users/Victor/Desktop/Ticker Data/{ticker_name}'

#Export ticker data to csv format
df.to_csv(f'{file_path}.csv')

#Plot Ticker Data
mpf.plot(df, 
        figratio = (20,12),
        title = ticker_name,
        type = 'candle',
        mav = (30,60,365),
        volume = True, 
        tight_layout = False,
        style = 'yahoo')

