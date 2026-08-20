import yfinance as yf
import pandas as pd
from datetime import datetime, timedelta

class DataIngestor:
    def __init__(self, symbols=["AAPL", "MSFT", "GOOGL", "BTC-USD"]):
        self.symbols = symbols

    def fetch_historical_data(self, period="1y", interval="1d"):
        """
        Fetches historical data for the defined symbols using yfinance.
        """
        data = {}
        for symbol in self.symbols:
            print(f"Fetching data for {symbol}...")
            ticker = yf.Ticker(symbol)
            df = ticker.history(period=period, interval=interval)
            data[symbol] = df
        return data

    def save_to_csv(self, data, directory="data/raw"):
        import os
        if not os.path.exists(directory):
            os.makedirs(directory)

        for symbol, df in data.items():
            path = os.path.join(directory, f"{symbol}_history.csv")
            df.to_csv(path)
            print(f"Saved {symbol} data to {path}")

if __name__ == "__main__":
    ingestor = DataIngestor()
    historical_data = ingestor.fetch_historical_data()
    ingestor.save_to_csv(historical_data)
