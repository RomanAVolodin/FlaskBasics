from flask import Blueprint, render_template, current_app
import requests

stock = Blueprint('stock', __name__, url_prefix='/stock')

API_URL = '{base_url}stock/real-time-price/{ticker}'


def fetch_price(ticker):
    data = requests.get(
        API_URL.format(ticker=ticker.upper(), base_url=current_app.config['STOCK_API_BASE_URL']), params={'apikey': 'demo'}
    ).json()
    return data['price']


def fetch_income(ticker):
    url = f'{current_app.config["STOCK_API_BASE_URL"]}/financials/income-statement/{ticker}'
    result = requests.get(url, params={'period': 'quarter', 'apikey': 'demo'}).json()['financials']
    result.sort(key=lambda quarter: quarter['date'])
    return result


@stock.route('/<string:ticker>')
def quote(ticker):
    price = fetch_price(ticker)
    return render_template('stock/quote.html', ticker=ticker.upper(), price=price)


@stock.route('/<string:ticker>/financials')
def financials(ticker):
    data = fetch_income(ticker)
    return render_template('stock/financials.html', ticker=ticker.upper(), financials=data)