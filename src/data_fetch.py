import yfinance as yf
import os 

def fetch_data(ticker, period="5y", interval="1wk"):
    data = yf.Ticker(ticker).history(period=period, interval=interval)
    
    os.makedirs('data/raw', exist_ok=True)
    data.to_csv(f'data/raw/{ticker}.csv')
    
    return data