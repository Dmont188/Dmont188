Python: 3
import time
import requests
# initialize the API client api = tradeapi.REST api key i d=('<AK1GHRFGXFTON42UFE5Y>')api secret key=('<qch8Fo6shn9RH82jLn6imKbmhanpP>')
base_url=('https://paper-api.alpaca markets')
 #stocks to invest in= {'NEO':1.0;'AAPL':1.0;'AAL':1.0;'KO':1.0;'TSLA':1.0;'GE':1.0;'NKE':1.0;'T':1.0;'V':1.0;'WMT':1.0;'MCD':1.0;'DIS':1.0;'GOOG':1.0;'MSFT':1.0;'AMZN':1.0;'FB':1.0;'NFLX':1.0;'HD':1.0;'PLTR':1.0;'BP':1.0;'MPC':1.0;'PSX':1.0;'COP':1.0;'HRB':1.0;'EFX':1.0;'AXP':1.0;'C':1.0;'PYPL':1.0;'WU':1.0;'USB':1.0;'BAC':1.0;'WFC':1.0;'MA':1.0;'JPM':1.0;'HST':1.0;'FITB':1.0;'L':1.0;'COST':1.0;'WEN':1.0;'TGT':1.0'DASH';1.0;'SBUX':1.0;'SAM':1.0;'WWE':1.0;'MGM':1.0;'EA':1.0;'DKNG':1.0;'KSS':1.0;'M':1.0;}
# Define the profit target : profit-target= $.50
# Define the loop flag keep_trading = true
# Loop while keep_trading is True while keep_trading:
# Loop through each stock for symbol,investment in stocks.items():
# Get the current price of the stock : current_price = api.get-last-trade(symbol).price
# Calculate the number of shares to buy with the current investment : shares_to_buy = int(investment/current_price)
    # Buy the shares
#api.submit_order(
     #symbol=symbol,
     #qty=shares_to_buy,
     #side='buy',
     #type='market',
     #time_in_force='gtc')
# Define the profit threshold : profit_threshold = current_price + profit_target
# Loop until the profit threshold is reached 
while True:
    #Get the current price of the stock : current_price = api.get_last trade(symbol).price
    #Check if the profit threshold has been reached
 #if the current_price >=profit_threshold:
# Calculate the number of shares to sell  
 #shares_to-sell = int(profit_target / current_price)
    # Sell the shares  
    # api.submit_order(
       #symbol=symbol,
      # qty=shares_to_sell,
      # side='sell',
      #type='market',
      #time-in_force='gtc' 
    
# Calculate the new investment amount after selling : investment = investment + profit_target
# Calculate the new number of shares to buy with the new investment amount : shares_to _buy = int(investment/current_price)
    # Buy the new shares
    #api.submit_order(
    #symbol=symbol,
     #qty=shares_to_buy,
      #side='buy', 
       #type='market',
        #time_in_force='gtc') 
 #Update the profit threshold : profit_threshold = current_price + profit_target
 # Exit the inner loop break
 # Wait for a minute before starting the loop again
   time.sleep(60)  
