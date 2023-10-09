# Project Name

This project is a Python Flask API app that fetches data from Yahoo Finance, analyzes the indicators, and sends indicator signals to users via LINE messaging API.

## Installation

1. Clone the repository.
2. Install the required packages using `pip install -r requirements.txt`.
3. Run `python app.py` to start the server.

## Usage

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
