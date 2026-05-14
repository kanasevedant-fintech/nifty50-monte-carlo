import pandas as pd
import yfinance as yf
import os

def download_data(ticker, start, end, interval, save_path):
    if os.path.exists(save_path):
        print(f"Loading data from {save_path}...")
        df = pd.read_csv(save_path, index_col=0, parse_dates=True)
        df["Close"] = pd.to_numeric(df["Close"], errors="coerce")  # ensure Close is float, not string
        df = df.dropna()
        return df
    else:
        print(f"Downloading data for {ticker} from {start} to {end}...")
        df = yf.download(ticker, start=start, end=end, interval=interval)
        if isinstance(df.columns, pd.MultiIndex):  # flatten multi-level columns from yfinance
            df.columns = df.columns.get_level_values(0)
        df = df[["Close"]].dropna()
        df.to_csv(save_path)
        return df
