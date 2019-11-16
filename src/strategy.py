from indicators import Rsi
from operation import Operation

class Strategy:

	RSI_DAYS = 14
	RSI_MIN = 30
	RSI_MAX = 70

	def __init__(self):
		self._rsi = Rsi(days=self.RSI_DAYS)
		self._rsi_count_days = self.RSI_DAYS
		self._rsi_threshold = [self.RSI_MIN, self.RSI_MAX]
		self._rsi_last = 0

	def _analyze(self, stock, price, wallet):
		signal = {'action' : Operation.NEUTRAL, 'qnt' : 0}

		if self._rsi_count_days > 0:
			self._rsi.update(price['close'])
			self._rsi_count_days -= 1
			return signal

		else:
			strengh = self._rsi.getRsi()

			if strengh > self._rsi_threshold[1]:
				signal['action'] = Operation.SELL
				qnt = price['open'] * stock['qnt'] / (price['open'] + stock['pm'])
				qnt_r = qnt % 100
				if qnt_r > 50:
					qnt_r = 100
				else:
					qnt_r = 0
				
				qnt_q = int(qnt / 100)
				
				signal['qnt'] = qnt_q * 100 + qnt_r

			if strengh < self._rsi_threshold[0]:
				signal['action'] = Operation.BUY
				qnt = wallet.getRessources() / price['open']
				qnt_r = qnt % 100
				if qnt_r > 50:
					qnt_r = 100
				else:
					qnt_r = 0
				
				qnt_q = int(qnt / 100)
				
				signal['qnt'] = qnt_q * 100 + qnt_r

			self._rsi_last = strengh
			self._rsi.update(price['close'])

			return signal

	def evalueate(self, stock, price, wallet):
		return self._analyze(stock, price, wallet)