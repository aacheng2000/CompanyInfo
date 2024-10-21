import json
from getJSON import getJSON as g
from io import BytesIO
import datetime

# Convert date to military time
def convert_timestamp(unix_timestamp):
    convertedTimestamp = datetime.datetime.fromtimestamp(unix_timestamp)
    time_only = convertedTimestamp.time()
    return time_only
    #return convertedTimestamp

# Input: stock symbol => output: timestamps and closing values
def getArray(symbol, timeSpan):
    closeArray = []
    timeArray = []
    apiHost = "yahoo-finance-api-data.p.rapidapi.com"
    url = "https://yahoo-finance-api-data.p.rapidapi.com/chart/simple-chart?symbol=" + symbol+ "&limit=10&range=" + str(timeSpan)
    # 1d, 5d, 1mo, 3mo, 6mo, 1y, 2y, 5y, 10y, ytd, max
    response = g(url,apiHost)
    # print ('=========' + str(response) + '===========')
    if str(response['message'])[:5] == 'Error':
        return [0],[0],0    
    close = response['data'][0]['indicators']['quote'][0]['close']
    timestamp = response['data'][0]['timestamp']
    
    # Loop
    for i in timestamp:
        #print('type of i in timestamp = ' + str(type(i)))
        formattedDate = datetime.datetime.fromtimestamp(i) #convert_timestamp(i)
        #timeArray.append(formattedDate.strftime('%H:%M'))
        timeArray.append(formattedDate)
        #timeArray.append(i)

    for i in close:
        closeArray.append(i)
    return timeArray,closeArray, len(timestamp)

# print(getArray()[0])