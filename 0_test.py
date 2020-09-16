from ib_insync import *
import nest_asyncio
nest_asyncio.apply()

ib = IB()
ib.connect('127.0.0.1', 7497, clientId=11) #hostname/ip, port, clientID for this client(unique)

# contracts = [Forex(pair) for pair in ('EURUSD', 'USDJPY', 'GBPUSD', 'USDCHF', 'USDCAD', 'AUDUSD')]
contracts = [Option(pair) for pair in ('AAPL', 'AMD')]
fixed_contracts = ib.qualifyContracts(*contracts)

ticker = []
for contract in fixed_contracts:
    ticker = ib.ticker(ib.reqMktData(contract=contract, genericTickList='', snapshot=True, regulatorySnapshot=False))

print(ticker[0])

ib.disconnect()
