import yfinance as yf
import pandas as pd

"""
Fetch data from yfinance
"""
def fetch_yfinance_data (
    tickers, 
    interval,
    period = None,
    start = None,
    end = None,
):
  if (period):
    dataF = yf.download(
      tickers = tickers, 
      interval = interval,
      period = period
    )
  else:
    dataF = yf.download(
      tickers = tickers, 
      interval = interval,
      start = start,
      end = end
    )

  df = pd.DataFrame(dataF)

  # use df index, convert DateTime to  a column instead of index
  df.reset_index(inplace=True)

  # delete Adj Close
  df = df.drop(['Adj Close'], axis=1)

  # rename Datetime to "Gmt time"
  df = df.rename(columns={'Datetime':'Gmt time'})

  df['Gmt time']=pd.to_datetime(df['Gmt time'],format='%d.%m.%Y %H:%M:%S')
  df.set_index("Gmt time", inplace=True)
  df=df[df.High!=df.Low]
  
  return df

def fetch_current_price (tickers):
  ticker_yahoo = yf.Ticker(tickers)
  data = ticker_yahoo.history()
  last_quote = data['Close'].iloc[-1]
  return str(last_quote)[:7]

