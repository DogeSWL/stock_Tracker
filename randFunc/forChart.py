import pandas as pd
import re

def getXY(type, url):
    xAxis = []
    yAxis = []
    infoList = pd.read_json(url)

    for x, y in infoList[type].items():
        # cleaning out bad data
        if not re.search('[a-zA-Z]',x):
            # separate day and time
            # append time data of ticker to xAxis
            tickTime = x.split(" ")
            xAxis.append(tickTime[1])

            for aX, xY in y.items():
                # grab data from close price of ticker
                # append data to yAxis list
                if "close" in aX:
                    yAxis.append(xY)

    xy = [xAxis, yAxis]

    return xy
