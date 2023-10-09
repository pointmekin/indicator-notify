# Project Name

This project is a Python Flask API app that fetches data from Yahoo Finance, analyzes the indicators, and sends indicator signals to users via LINE messaging API.

| Official Account | Demo |
| --- | --- |
| ![Screenshot 2023-10-10 at 02 23 26](https://github.com/pointmekin/indicator-notify/assets/53035529/f016788f-9762-414d-82b8-8daf51e5ae61) | ![IMG_893337966272-1](https://github.com/pointmekin/indicator-notify/assets/53035529/0da0ac06-dc48-4694-88a5-1780a30bbd9d) |

## Installation

1. Clone the repository.
2. Install the required packages using `pip install -r requirements.txt`.
3. Run `python app.py` to start the server.

## Indicator Signals Usage

1. Add the **Indicator Notify** LINE Official Account

   Scan the QR code
   
   <img src="https://github.com/pointmekin/indicator-notify/assets/53035529/7cec34e7-e305-4613-bdc3-9deab4367a62" width="200" />

   Or add the official account using the ID: **@897vuilz**

3. Wait for indicator signals!

## Code Usage

1. Send a GET request to `/get-signals` with the following parameters:
    - `symbol`: The stock symbol you want to analyze.
    - `interval`: The time interval for the data (e.g., 1d, 1wk, 1mo).
    - `period`: The backwards period of the data from yfinance used to plot the indicators
2. The API will return a JSON object with the following fields:
    - `LINE_messages`: The LINE message sent including the symbol, interval, summary of indicator signal, and the current asset price
    - `response`: The response from LINE messaging API

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [yfinance](https://pypi.org/project/yfinance/) for providing the financial data
- [LINE Developers](https://developers.line.biz/en/) for providing the messaging API.

Please let me know if you need any further assistance.
