import pandas as pd 
import os

def process_data(ticker):
    path = f'data/raw/{ticker}.csv'
    df = pd.read_csv(path, index_col="Date", parse_dates=True)
    
    df["MA20"] = df["Close"].rolling(window=20).mean()
    df["MA50"] = df["Close"].rolling(window=50).mean()
    
    os.makedirs('data/processed', exist_ok=True)
    df.to_csv(f'data/processed/{ticker}_processed.csv')
    
    return df
