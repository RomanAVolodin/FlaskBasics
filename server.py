from flask import Flask
import requests

app = Flask(__name__)

API_URL = 'https://financialmodelingprep.com/api/v3/stock/real-time-price/{ticker}'


def fetch_price(ticker):
    data = requests.get(
        API_URL.format(ticker=ticker), params={'apikey': 'demo'}
    ).json()
    return data['price']


@app.route('/stock/<ticker>')
def stock(ticker):
    price = fetch_price(ticker)
    return f'The price of {ticker} id {price}'


@app.route('/')
def home_page():
    return 'Try /stock/AAPL'


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
