from flask import Flask, render_template
from stock_app.blueprints.stock import stock
from stock_app.blueprints.home import home
from stock_app.config import DevConfig, ProdConfig, TestConfig


def create_app(environment_name='dev'):
    app = Flask(__name__)

    if environment_name == 'dev':
        app.config.from_object(DevConfig)
    elif environment_name == 'test':
        app.config.from_object(TestConfig)
    else:
        app.config.from_object(ProdConfig)

        @app.errorhandler(500)
        def handle_error(exception):
            return render_template('500.html'), 500

    app.register_blueprint(stock)
    app.register_blueprint(home)
    return app

