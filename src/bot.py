from operation import Operation
from prices import Prices
from time import sleep

class Bot:

	def __init__(self, wallet, ticker=None, strategy=None):
		self._on_off = True
		self._ticker = ticker
		self._strategy = strategy
		self._wallet = wallet
		self._prices = Prices(self._ticker)

	def start(self):
		while self._on_off:
			stocks = self._wallet.getAllStocks()

			for stock in stocks:
				price = self._prices.getNextPrice(stock['ticker'])
				signal = self._strategy.evalueate(stock, price, self._wallet)

				if signal['action'] != Operation.NEUTRAL:
					operation = Operation(signal['action'], stock['ticker'], price['open'], signal['qnt'])

					if self._validateOperation(operation):
						self._operate(operation)

	def _operate(self):
		self._wallet.update(operation):
		print(operation)
		
	def _validateOperation(self, operation):
		operation_data = operation.getOperationData()

		if operation_data['type'] == Operation.BUY: 
			wallet_ressources = self._wallet.getFreeRessources()
			operation_cost = operation_data['qnt'] * operation_data['price']

			if wallet_ressources >= operation_cost:
				return True
			else:
				return False

		elif operation_data['type'] == Operation.SELL:
			stock = self._wallet.getStock(operation_data['ticker'])

			if stock['qnt'] > operation_data['qnt']:
				return True
			else:
				return False

		else:
			return False