from os import system, name
from subprocess import call
def clear():

    _ = call('clear' if name =='posix' else 'cls')
    # if name == 'nt':
    #     _ = system('cls')
    # else:
    #     _ = system('clear')

# clear()

import shrimpy
import time
from datetime import datetime
import math
import sys

def center(rng):
    l = len(rng)
    sp = 37-(l/2)
    ret = rng
    for i in range(int(sp)):
        ret = " "+ret

    return ret


c = 0
speed = 1
# coin = input("Coin:")
margin = 1.0001
sold = ' '


def check(stry):
    clear()
    print("<------------------------------ STARTING UP ------------------------------>")
    global c
    c += 1
    ch = str(c)
    s1 = center("Check"+ch+", passed")
    print("\n"+s1+"\n\n"+stry)
    time.sleep(1)
    # clear()


def finalCheck():
    global c
    c += 1
    ch = str(c)
    # print("Check"+ch+", passed"+"\n\n")
    clear()

clear()
check(center("Libraries imported and margin set")) #1
time.sleep(1)

exchange_name = "binance"
exchange_public_key = 'o9pweDdKtniUw2uF94Sl87V4pThUWggSvPHmSw2xI4OrIsElhHTJSYAI9A3NeCYa'
exchange_secret_key = 'TJWj7QHdUNkgCHZbPky7lo0dAMEiMrMGz3LVrQJWcYjCWwFayelCwxFQMRvXz6sp'

shrimpy_public_key = 'eb3b30e4cceb52907166182a1b7c718fa39e3c7e206c9ab7dc0d6486f234a176'
shrimpy_secret_key = '1d926f3bcbff631b0e8b93aad9cc7d3c0d886ad5b9e3589e86669a59d31f2fad784f8cbadcd009bd951ee630971ff0fbc6bc20c0dfd7da020e9a65ce097c6418'

def error_handler(err):
    print(err)

# Create the websocket client
api_client = shrimpy.ShrimpyApiClient(shrimpy_public_key, shrimpy_secret_key)
raw_token = api_client.get_token()
ws_client = shrimpy.ShrimpyWsClient(error_handler, raw_token['token'])

clear()
check(center("Client all set")+"\n"+center("Error handler ready")) #2
time.sleep(speed)
# Create a user which will be linked to our exchange
# Skip this step (or use the "list users" endpoint) if you've already created a user
# create_user_response = api_client.create_user('The Shrimp Master')
# user_id = create_user_response['id']
user_id = 'cbc3dd48-e823-472c-a7e6-2219ed8fe0bb'

# Link our first exchange so we can access balance data
# Skip this step (or use the "list accounts" endpoint) if you've already linked an account
# link_account_response = api_client.link_account(
#     user_id,
#     exchange_name,
#     exchange_public_key,
#     exchange_secret_key
# )

account_id = '67114'

# Wait while Shrimpy collects data for the exchange account
# Only required the first time linking
# time.sleep(5)

# Access balance data for the user account you previously created
balance = api_client.get_balance(
    user_id,   # user_id
    account_id # account_id
)

clear()
check(center("Got balance and entered user ID")) #3
time.sleep(speed)

btcAmount = 0
coinAmount = 0
boughtAt = 0
sellprice = ''
willsell = ''
upby = 'egg'
dec = ''
oglen = 0

county = 0

for asset in balance['balances']:
    if asset['symbol'] == 'BTC':
        btcAmount = asset['nativeValue']

# print("btcAmount"+str(btcAmount))
clear()
check(center("Basic variables declared")+"\n"+center("Quantity of BTC determined")) #4
time.sleep(speed)

def sell(coni):
    global balance
    balance = api_client.get_balance(
        user_id,   # user_id
        account_id # account_id
    )
    holdings = balance['balances']
    consolidation_symbol = str(coni)
    for asset in holdings:
        asset_symbol = asset['symbol']
        asset_amount = asset['nativeValue']
        if asset_symbol != consolidation_symbol:
            # print('Selling ' + str(asset_amount) + ' of ' + asset_symbol)
            create_trade_response = api_client.create_trade(
                user_id,
                account_id,
                asset_symbol,
                consolidation_symbol,
                asset_amount
            )



def handler(msg):
    global tim1
    global tim2
    global tim3
    global btcAmount
    global coinAmount
    global boughtAt
    global price
    global pric
    global balance
    global sold
    global sellprice
    global willsell
    global upby
    global dec
    global oglen
    global marg
    global county
    if tim2 == 0:
        tim2 = time.perf_counter()
        print("Timing: "+str(tim2-tim1))

    balance = api_client.get_balance(
        user_id,   # user_id
        account_id # account_id
    )
    pric = msg['content'][0]['price']
    price = float(pric)
    if coinAmount == 0:
        coinAmount = math.floor(btcAmount/price)
        amount = round(((coinAmount*price)-0.00000001),8)
        ant = str(btcAmount)
        smart_order_response = api_client.create_trade(
            user_id,    # user_id
            account_id, # account_id
            'BTC',            # from_symbol
            coin,           # to_symbol
            ant        # amount of from_symbol
            # True
        )
        if tim3 == 0:
            tim3 = time.perf_counter()
            print("Aditional Timing: "+str(tim3-tim2))
        print(smart_order_response)
        boughtAt = price
        for asset in balance['balances']:
            if asset['symbol'] == coin:
                coinAmount = asset['nativeValue']
        print("Bought "+str(coinAmount)+" of "+str(coin)+" for "+str(boughtAt)+" per coin.")
        willsell = '   Will Sell At: '+str(round(((boughtAt*margin)+0.0000005),6))
        time.sleep(1)

    elif price > (boughtAt*margin) or price<(boughtAt*0.99):

        if sold != '  SOLD AT: ':
            sell('BTC')
            sold = '  SOLD AT: '

            prec = (100*((price-boughtAt)/boughtAt))
            if prec> 0.01 or prec<(0-0.01):
                prec = round(prec, 2)
            else:
                prec = round(prec, 6)

            if prec > 0:
                upby = '!!  Profit of: %'+str(prec)
            else:
                upby = '  :(  Loss of: %'+str(abs(prec))

            sellprice = str(price)+upby
            willsell = ''
            upby = ''
            marg = ''
            county = 0


        # ws_client.disconnect()
    if upby != '':
        prec = (100*((price-boughtAt)/boughtAt))
        if prec> 0.01 or prec<(0-0.01):
            prec = round(prec, 2)
        else:
            prec = round(prec, 6)

        if prec > 0:
            upby = '   Up By:   %'+str(prec)
        else:
            upby = '   Down By: %'+str(abs(prec))

    lenny = len(str(price-math.floor(price)))
    if oglen == 0:
        oglen = lenny
    else:
        if lenny==oglen:
            dec = ''
        elif (lenny+2)==oglen:
            dec = '00'
        else:
            dec = '0'

    county = county+1

    if sold != '  SOLD AT: ':
        print("Price: "+str(price)+dec+"  Bought At: "+str(boughtAt)+willsell+marg+upby+sold+sellprice)
    elif county == 3:
        ws_client.disconnect()
        county = 900
        clear()
        time.sleep(1)
        print("<------------------------------ SALE REPORT ------------------------------>\n")
        print(center("Bought At: "+str(boughtAt)+willsell+marg+upby+sold+sellprice))
        time.sleep(25)




clear()
check(center("All functions set up and ready to go")) #5

time.sleep(speed)
clear()
time.sleep(1)
print("<--------------------------------- READY --------------------------------->\n")
margy = input("Margin:")

if margy == "" or margy == "test" or margy == "Test" or margy == "TEST" or margy == "default" or margy == "Default" or margy == "DEFAULT":
    margie = 1
else:
    margie = float(margy)


if margie>100:
    margin = (margie/100)
elif margy == "" or margy == "test" or margy == "Test" or margy == "TEST":
    margin = 1.0001
elif margy == "default" or margy == "Default" or margy == "DEFAULT":
    margin = 2
else:
    margin = margie

marg = '   Margin: %'+str((margin*100))
time.sleep(1)
clear()
time.sleep(1)
print("<----------------------------- PROFIT MARGIN ----------------------------->\n\n")
print(center("Margit is set to %"+str(margin*100)))
time.sleep(3)
clear()
time.sleep(1)
print("<--------------------------------- READY --------------------------------->\n")

coin = input("Coin:")

tim1 = time.perf_counter()
tim2 = 0
tim3 = 0

coinPair = coin+"-btc"

subscribe_data = {
    "type": "subscribe",
    "exchange": "binance",
    "pair": coinPair,
    "channel": "trade"
}

# Start processing the Shrimpy websocket stream!
finalCheck() #6
ws_client.connect()
ws_client.subscribe(subscribe_data, handler)
