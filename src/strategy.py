from indicators import Rsi
from operation import Operation

class Strategy:

	def __init__(self, days=5):
		self._rsi = Rsi(days=days)
		self._days = days
		self._rsi_threshold = [50, 52]

		self._rsi_last = 0

	def _evaluate(self, wallet, price):
		signal = {'action' : Operation.NEUTRAL, 'qnt' : 0 }
		strengh = self._rsi.getRsi()

		if strengh > self._rsi_threshold[1]:
			signal['action'] = Operation.SELL
			stock = wallet.getStock('BPAN4')
			qnt = price * stock['qnt'] / (price + stock['pm'])
			print(qnt) 
			qnt_r = qnt % 100
			print("1")
			
			print("2")
			if qnt_r > 50:
				qnt_r = 100
			
			print("3")
			qnt_q = int(qnt / 100)
			
			print("4")
			signal['qnt'] = qnt_q * 100 + qnt_r
			print(signal)

		if strengh < self._rsi_threshold[0]:
			signal['action'] = Operation.BUY
			signal['qnt'] = 100

		return signal

	def lookThisWalletAndPriceAndGiveMeSignal(self, wallet, price):
		try:
			self._rsi_last = self._rsi.getRsi()

			signal = self._evaluate(wallet, price)

			self._rsi.update(price['close'])

			return signal
		except:
			self._rsi.update(price['close'])
			return {'action' : Operation.NEUTRAL, 'qnt' : 0 }