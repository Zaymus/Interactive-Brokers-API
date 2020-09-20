from ib_insync import *
import nest_asyncio
nest_asyncio.apply()

ib = IB()
ib.connect('127.0.0.1', 7497, clientId=11) #hostname/ip, port, clientID for this client(unique)

contracts = ib.reqContractDetails(Option(symbol='AAPL'))
dt = ''
barsList = []
while True:
    bars = ib.reqHistoricalData(
        contracts[0],
        endDateTime=dt,
        durationStr='10 D',
        barSizeSetting='1 day',
        whatToShow='MIDPOINT',
        useRTH=True,
        formatDate=1)

    if not bars:
        break
        
    barsList.append(bars)
    dt = bars[0].date
    print(dt)

ib.disconnect() #disconnects from the IB API(necessary for the clientId to be reused)
