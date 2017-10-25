from flask import redirect, render_template
from app import app
import requests
from assets import api_key

from randFunc.forChart import getXY

keyAPI = api_key.a

@app.route("/index")
def home():
    url = "https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=MSFT&interval=30min&apikey=" + keyAPI

    chartXY = getXY("Time Series (30min)", url)

    legend = "Price"
    times = chartXY[0]
    prices = chartXY[1]

    return render_template('index.html', values=prices, labels=times, legend=legend)

@app.route("/")
def index():
    return redirect('/index')

if __name__ == "__main__":
    app.run()
