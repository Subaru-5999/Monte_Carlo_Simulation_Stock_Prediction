import numpy as np
import pandas as pd
import yfinance as yf
from datetime import datetime
import pytz

def get_stock_data(ticker, start="2022-01-01"):
    india_tz = pytz.timezone('Asia/Kolkata')
    now_ist = datetime.now(india_tz)
    end = now_ist.strftime("%Y-%m-%d")

    data = yf.download(ticker, start=start, end=end)
    if data.empty:
        raise ValueError(f"Stock '{ticker}' does not exist or data is unavailable.")

    live_data = yf.Ticker(ticker).history(period="1d", interval="1m")
    if not live_data.empty:
        S0 = float(live_data["Close"].iloc[-1])
    else:
        S0 = float(data["Close"].iloc[-1])

    data["LogReturn"] = np.log(data["Close"] / data["Close"].shift(1))
    data = data.dropna()

    return S0, data["LogReturn"].to_numpy()
