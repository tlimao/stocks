from operation import Operation

class Wallet:

	def __init__(self, ressources):
		self._initial_ressources = ressources
		self._free_ressources = ressources
		self._free_ressources_by_stock = {}
		self._wallet_price = ressources
		self._stocks = {}

	def update(self, operation):
		operation_data = operation.getOperationData()

		ticker = operation_data['ticker']
		typeo  = operation_data['type']
		qnt    = operation_data['qnt']
		price  = operation_data['price']

		if ticker in self._stocks:
			stock_data = self._stocks[ticker]

			if typeo == Operation.BUY:

				new_qnt = stock_data['qnt'] + qnt
				self._free_ressources -= price * qnt
				new_pm = (stock_data['qnt'] * stock_data['pm'] + price * qnt)/new_qnt

				self._stocks[ticker].update({'pm' : new_pm, 'qnt' : new_qnt, 'price' : price})

			else:
				new_qnt = stock_data['qnt'] - qnt
				self._free_ressources += price * qnt

				if new_qnt == 0:
					del self._stocks[ticker]
				else:
					self._stocks[ticker].update({'qnt' : new_qnt, 'price' : price})

		else:
			if typeo == Operation.BUY:
				self._free_ressources -= price * qnt
				self._stocks[ticker] = {'pm' : price, 'qnt' : qnt, 'ex' : 0,  'price' : price, 'return' : 0}

		self.updateBalances(ticker, price)

	def getStock(self, ticker):
		return self._stocks[ticker]

	def getAllStocks(self):
		return self._stocks

	def updateBalances(self, ticker, price):
		if self._stocks[ticker] != None:
			total_budget = 0

			self._stocks[ticker].update({'price' : price})

			for key, value in self._stocks.items():
				total_budget += value['price'] * value['qnt']

			for key, value in self._stocks.items():
				if value['pm'] != 0:
					value.update({'ex' : value['price'] * value['qnt'] / total_budget })
					value.update({'return' : (value['price'] - value['pm']) / value['pm']})

			self._wallet_price = total_budget + self._free_ressources

	def __str__(self):
		wallet_str =  ""
		for key, value in self._stocks.items():
			stock_str = "{ticker} [Price: {price} | Pm: {pm} | Qnt: {qnt} | Total: {total} | Ex: {ex} | Return: {rreturn}]\n"
			wallet_str += stock_str.format(
				ticker  = key,
				price   = round(value['price'], 2),
				pm      = round(value['pm'], 2),
				qnt     = value['qnt'],
				total   = value['qnt'] * value['price'],
				ex      = str(round(value['ex'] * 100, 2)) + "%",
				rreturn = str(round(value['return'] * 100, 2)) + "%"
			)

		wallet_str += "\nReturn Total: " + str(self.getReturn()) + "% (" + str(self._wallet_price) + ")"

		return wallet_str

	def getReturn(self):
		return round(100 * (self._wallet_price - self._initial_ressources ) / self._initial_ressources, 2)

	def getWalletPrice(self):
		return self._wallet_price

	def getRessources(self):
		return self._free_ressources

	def addStock(self, ticker):
		self._stocks[ticker] = {'pm' : 0, 'qnt' : 0, 'ex' : 0,  'price' : 0, 'return' : 0}