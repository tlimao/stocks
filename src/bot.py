from operation import Operation
from prices import Prices
from time import sleep

class Bot:

	MODE_REAL = 1
	MODE_SIMULATED = 0

	def __init__(self, wallet, ticker=None, strategy=None, start_date=None, mode=MODE_SIMULATED):
		self._on_off = True
		self._ticker = ticker
		self._strategy = strategy
		self._wallet = wallet
		self._prices = Prices(self._ticker)
		if start_date != None:
			self._prices.setDatePoint(start_date)
		self._mode = mode

	def start(self):
		while self._on_off:
			stock_info = self._wallet.getStock(self._ticker)
			price = self._prices.getNextPrice()
			signal = self._strategy.evalueate(stock_info, price, self._wallet)

			if signal['action'] != Operation.NEUTRAL:
				operation = Operation(signal['action'], self._ticker, price['open'], signal['qnt'])

				if self._validateOperation(operation):
					self._operate(operation)

			self._on_off = self._prices.hasNext()

	def _operate(self, operation):
		self._wallet.update(operation)
		print(operation)
		
	def _validateOperation(self, operation):
		operation_data = operation.getOperationData()

		if operation_data['type'] == Operation.BUY: 
			wallet_ressources = self._wallet.getRessources()
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