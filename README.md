# Stock_ETL
A beginner-friendly Python project that demonstrates how to build a simple ETL (Extract, Transform, Load) pipeline using the [yFinance](https://pypi.org/project/yfinance/) API. The script fetches historical stock data, computes moving averages, summarizes key financial statistics, and exports the results to CSV files.

---

## 🚀 Features

- Accepts single or multiple stock tickers (e.g., AAPL, TSLA, MSFT)
- Fetches historical stock data using `yfinance`
- Calculates 20-day moving average (MA20)
- Outputs summary statistics:
  - Highest & lowest closing price
  - Total trading days
  - Average trading volume
- Saves processed data to `.csv`
- Generates a line chart with optional moving average

---

## 🛠️ Tech Stack

- Python 3.x
- yFinance
- Pandas
- Matplotlib

---

## 📦 Installation

```bash
git clone https://github.com/yourusername/stock-etl-project.git
cd stock-etl-project
pip install -r requirements.txt
python stock_etl.py
