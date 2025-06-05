import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
import os

# --- Setup ---
# Create data directory if not exists
if not os.path.exists("data"):
    os.makedirs("data")

# Get user input
tickers = input("Enter stock tickers separated by commas (e.g., AAPL, MSFT, TSLA): ")
tickers = [t.strip().upper() for t in tickers.split(",")]

# Define date range
start_date = "2024-01-01"
end_date = datetime.today().strftime('%Y-%m-%d')

# --- Loop through tickers ---
for ticker_symbol in tickers:
    print(f"\n=== Processing {ticker_symbol} ===")
    
    try:
        # --- Extract ---
        data = yf.download(ticker_symbol, start=start_date, end=end_date)

        if data.empty:
            print(f"⚠️ No data found for {ticker_symbol}. Skipping...")
            continue

        # --- Transform ---
        data = data[['Open', 'High', 'Low', 'Close', 'Volume']]
        data['MA20'] = data['Close'].rolling(window=20).mean()

        # --- Stats ---
        print(f"\n--- Summary for {ticker_symbol} ---")
        print(f"Date Range: {start_date} to {end_date}")
        print(f"Total Trading Days: {len(data)}")
        print(f"Highest Closing Price: ${float(data['Close'].max()):.2f}")
        print(f"Lowest Closing Price: ${float(data['Close'].min()):.2f}")
        print(f"Average Volume: {float(data['Volume'].mean()):,.0f} shares")

        # --- Load ---
        filename = f"data/{ticker_symbol}_stock_data.csv"
        data.to_csv(filename)
        print(f"✅ Data saved to {filename}")

        # --- Optional Plot for last ticker ---
        if ticker_symbol == tickers[-1]:
            plt.figure(figsize=(12, 6))
            plt.plot(data['Close'], label='Close Price')
            plt.plot(data['MA20'], label='20-Day MA', linestyle='--')
            plt.title(f"{ticker_symbol} Stock Price")
            plt.xlabel("Date")
            plt.ylabel("Price (USD)")
            plt.legend()
            plt.grid(True)
            plt.tight_layout()
            plt.show()

    except Exception as e:
        print(f"❌ Error processing {ticker_symbol}: {str(e)}")
