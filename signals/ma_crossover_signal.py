from signals.yfinance_data import fetch_yfinance_data, fetch_current_price
import pandas_ta as ta
import requests
import json
import os


def TotalSignal(df, l):
    if (
        df.MACDSignal[l] == 1
    ):
        return 2
    if (
        df.MACDSignal[l] == -1
    ):
        return 1
    return 0


def ma_crossover_signal(
    tickers,
    interval,
    period=None,
    start=None,
    end=None,
):

    if (period is not None):
        df = fetch_yfinance_data(
            tickers=tickers,
            interval=interval,
            period=period
        )
    else:
        df = fetch_yfinance_data(
            tickers=tickers,
            interval=interval,
            start=start,
            end=end
        )

    df["MACD"] = ta.macd(df.Close)['MACD_12_26_9']
    df["MACD_HIST"] = ta.macd(df.Close)['MACDh_12_26_9']
    df["MACD_SIGNAL"] = ta.macd(df.Close)['MACDs_12_26_9']

    backcandles = 15

    # calcualte macd signal
    macd_signal = [0]*len(df)
    for row in range(1, len(df)):
        if(
            df.MACD_SIGNAL[row] > df.MACD[row]
            and df.MACD_SIGNAL[row-1] < df.MACD[row-1]
        ):
            macd_signal[row] = 1
        elif (
            df.MACD_SIGNAL[row] < df.MACD[row]
            and df.MACD_SIGNAL[row-1] > df.MACD[row-1]
        ):
            macd_signal[row] = -1

    df['MACDSignal'] = macd_signal

    TotSignal = [0]*len(df)
    for row in range(backcandles, len(df)):  # careful backcandles used previous cell
        TotSignal[row] = TotalSignal(df, row)
    df['TotalSignal'] = TotSignal

    # send notification

    url = "https://api.line.me/v2/bot/message/broadcast"
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer " + os.environ.get("SECRET")
    }
    print("Bearer " + os.environ.get("SECRET"))
    
    # current price
    

    # cross up

    if df.iloc[-1].TotalSignal == 2:
        data = {
            "messages": [
                {
                    "type": "text",
                    "text": "📈 Symbol:{} \n⏰ Interval:{} \n\n💡 MACD crossover pattern detected towards the upside ⬆️\n\n🏷️Current price: {}".format(tickers, interval, fetch_current_price(tickers))
                }
            ]
        }
        response = requests.post(url, headers=headers, data=json.dumps(data))
        return {
            "LINE_messages": data['messages'],
            "response": response.json()
        }, 200

    # cross down

    elif df.iloc[-1].TotalSignal == 1:
        data = {
            "messages": [
                {
                    "type": "text",
                    "text": "📈 Symbol:{} \n⏰ Interval:{} \n\n💡 MACD crossover pattern detected towards the downside ⬇️\n\n🏷️Current price: {}".format(tickers, interval, fetch_current_price(tickers))
                }
            ]
        }
        response = requests.post(url, headers=headers, data=json.dumps(data))
        return {
            "LINE_messages": data['messages'],
            "response": response.json()
        }, 200

    return {
        "message": "No signal"
    }, 200
