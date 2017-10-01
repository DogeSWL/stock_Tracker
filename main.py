from flask import redirect, render_template, json
from app import app
import requests
from assets import api_key


@app.route("/index")
def home():
    keyAPI = api_key.a
    url = "https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=MSFT&interval=1min&apikey=" + keyAPI
    r = requests.get(url)
    data = r.json()

    return render_template('index.html', metaData=data['Meta Data'],
                                         tSeries_1Min=data['Time Series (1min)'])

@app.route("/")
def index():
    return redirect('/index')

if __name__ == "__main__":
    app.run()
