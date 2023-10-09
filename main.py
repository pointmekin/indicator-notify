import os
from flask import Flask, request
from signals.ma_crossover_signal import ma_crossover_signal
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def index():
  return "<h1>Hello world</h1>"

@app.route('/get-signals', methods=['GET'])
def get_signals():
  args = request.args
  print(args)
  symbol = args['symbol']
  interval = args['interval']
  start = None
  end = None
  period = None
  if (
    symbol is None
    or interval is None
  ):
    # return bad request JSON response
    return {
      "message": "Bad request"
    }, 400
  
  if ('period' not in args ):
    if (args['start'] is not None):
      start = datetime.strptime(args['start'], '%d/%m/%y %H:%M:%S')
    if (args['end'] is not None):
      end = datetime.strptime(args['end'], '%d/%m/%y %H:%M:%S')
    return ma_crossover_signal(
      tickers = symbol,
      interval = interval,
      start = start,
      end = end
    )
  else:
    
    return ma_crossover_signal(
      tickers = symbol,
      interval = interval,
      period = args['period'],
    )

if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port=int(os.environ.get("PORT", 8080)))