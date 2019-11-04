from bot import Bot
from strategy import Strategy
from wallet import Wallet
from time import sleep

TICKER = "BPAN4"

ressources = 10000

wallet = Wallet(ressources)

bot_rsi = Bot(wallet, TICKER, Strategy(5))

bot_rsi.start()
#input('Fim ...')