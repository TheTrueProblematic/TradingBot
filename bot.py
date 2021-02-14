import shrimpy
import time
from os import name
from subprocess import call
import sys


class bot:
    def error_handler(self, err):
        print(err)


class printBot(bot):
    def __init__(self):
        self.stream = False
        self.clearLog()

    def clear(self):
        _ = call('clear' if name == 'posix' else 'cls')
        self.logWrite('output.txt', '\n\n\n')
        self.logWrite('log.txt', '\n\n\n')

    def error_handler(self, err):
        self.print("Error", err)

    def titleCenter(self, text):
        l = len(text)
        sp = 36 - (l / 2)
        ret = text
        for i in range(int(sp)):
            ret = "-" + ret + "-"

        ret = "<" + ret + ">"
        return ret

    def center(self, text):
        l = len(text)
        sp = 37 - (l / 2)
        ret = text
        for i in range(int(sp)):
            ret = " " + ret

        return ret

    def wrap(self, text):
        l = len(text)
        ret = ""
        if l <= 37:
            return self.center(text)
        else:
            while l > 0:
                l = l - 37
                tmp = text[:37]
                text = text[37:]
                ret = ret + self.center(tmp) + "\n"

            return ret

    def clearLog(self):
        file = open("output.txt", "r+")
        file.truncate(0)
        file.close()

    def logWrite(self, filename, content):
        # import sys
        # print('This message will be displayed on the screen.')
        original_stdout = sys.stdout # Save a reference to the original standard output
        with open(str(filename), 'w') as f:
            sys.stdout = f # Change the standard output to the file we created.
            print(str(content)) #This message will be written to a file
            sys.stdout = original_stdout # Reset the standard output to its original value

    def fullPrint(self, content):
        self.logWrite('output.txt', content)
        self.logWrite('log.txt', content)
        print(str(content))

    def print(self, title, content):
        if self.stream:
            self.fullPrint(str(title)+": "+str(content))
        else:
            self.clear()
            time.sleep(1)
            full = self.titleCenter(str(title)) + "\n\n" + self.wrap(str(content))
            self.fullPrint(full)

    def startPrintStream(self):
        self.clear()
        time.sleep(1)
        self.stream = True

    def endPrintStream(self):
        self.clear()
        time.sleep(1)
        self.stream = False



class pumpBot(printBot):
    def __init__(self, exchange_public_key,exchange_secret_key, shrimpy_public_key, shrimpy_secret_key, user_id, account_id):
        super().__init__()
        self.ex_pub = exchange_public_key
        self.ex_sec = exchange_secret_key
        self.smp_pub = shrimpy_public_key
        self.smp_sec = shrimpy_secret_key
        self.user_id = user_id
        self.account_id = account_id
        self.client = shrimpy.ShrimpyApiClient(shrimpy_public_key, shrimpy_secret_key)
        self.balance = self.client.get_balance(user_id, account_id)
        self.coin = ''

    def getBalance(self):
        return self.balance

    def setBalance(self):
        self.balance = self.client.get_balance(self.user_id, self.account_id)

    def getRawToken(self):
        return self.client.get_token()

    def setCoin(self, coin):
        self.coin = coin.upper()

    def getCoin(self):
        return self.coin.upper()

    def coinPrompt(self):
        self.print('Enter Coin', ' ')
        coin = input("Coin: ")
        self.setCoin(coin)
        return coin.upper()

    def condense(self, coinName):
        self.setBalance()
        holdings = self.balance['balances']
        consolidation_symbol = str(coinName)
        for asset in holdings:
            asset_symbol = asset['symbol']
            asset_amount = asset['nativeValue']
            if asset_symbol != consolidation_symbol:
                create_trade_response = self.client.create_trade(
                    self.user_id,
                    self.account_id,
                    asset_symbol,
                    consolidation_symbol,
                    asset_amount
                )

    def limitSell(self, coinFrom, coinTo, limit):
        return coinFrom

    def fileCoin(self):
        f = open("coin.txt", "r")
        content = f.read()
        l = len(content)
        if l>0:
            return content
        else:
            return None
