from ib_insync import *
import nest_asyncio
nest_asyncio.apply()

ib = IB()
ib.connect('127.0.0.1', 7497, clientId=11) #hostname/ip, port, clientID for this client(unique)

contracts = [] #list of all contracts pulled from IB
symbol = ['AAPL', 'AMD'] #list of symbols being requested to pull
expiry = ['20200918', '20200925'] #list of expiry dates being requested to pull
strike = 0.0 #strike price requested
right = 'C' #P/PUT and C/CALL
contract_count = 0 #number of contracts pulled

#fills contracts based on requested information above^^^
for sym in symbol:
    for exp in expiry:
        contracts.append(ib.reqContractDetails(Option(symbol=sym, lastTradeDateOrContractMonth=exp, strike=strike, right=right)))

#counts the total number of contracts pulled
loop = 0
for count in range(len(contracts)):
    contract_count += len(contracts[count])
    if loop != 0:
        print("+", len(contracts[count]))
    else:
        print(" ", len(contracts[count]))
    loop += 1

print("------")
print("Number of contracts found: ", contract_count)

ib.disconnect() #disconnects from the IB API(necessary for the clientId to be reused)
