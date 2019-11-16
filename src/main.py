from bot import Bot
from strategy import Strategy
from wallet import Wallet
from time import sleep

TICKER_1 = "BPAN4"
TICKER_2 = "PETR4"
TICKER_3 = "GRND3"

ressources = 30000

wallet = Wallet(ressources)
wallet.addStock(TICKER_1)
#wallet.addStock(TICKER_2)
#wallet.addStock(TICKER_3)

bot_1 = Bot(wallet, TICKER_1, Strategy(), '2018-10-02')
bot_1.start()
#bot_2 = Bot(wallet, TICKER_2, Strategy(), '2018-10-02')
#bot_2.start()
#bot_3 = Bot(wallet, TICKER_3, Strategy(), '2018-10-02')
#bot_3.start()

print(wallet)