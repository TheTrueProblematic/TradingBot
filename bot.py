import shrimpy
import time
from os import name
from subprocess import call


class baseBot:
    def error_handler(self, err):
        print(err)


class printBot(baseBot):
    def clear(self):
        _ = call('clear' if name == 'posix' else 'cls')

    def titleCenter(self, text):
        l = len(text)
        sp = 35 - (l / 2)
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

    def print(self, title, content):
        self.clear()
        time.sleep(1)
        print(self.titleCenter(title) + "\n")
        print(self.wrap(content))


class pumpBot(printBot):
    def __init__(self, exchange_secret_key, shrimpy_public_key, shrimpy_secret_key, user_id, account_id):
        self.ex_pub = self
        self.ex_sec = exchange_secret_key
        self.smp_pub = shrimpy_public_key
        self.smp_sec = shrimpy_secret_key
        self.user_id = user_id
        self.account_id = account_id
        self.client = shrimpy.ShrimpyApiClient(shrimpy_public_key, shrimpy_secret_key)
        self.balance = self.client.get_balance(user_id, account_id)

    def getBalance(self):
        return self.balance

    def setBalance(self):
        self.balance = self.client.get_balance(self.user_id, self.account_id)

    def getRawToken(self):
        self.client.get_token()

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
