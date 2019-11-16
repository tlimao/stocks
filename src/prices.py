from datetime import datetime
from datetime import timedelta

class Prices:

	TIME_SERIES = {
		'TIME_SERIES_INTRADAY' : '%Y-%m-%d',
		'TIME_SERIES_DAILY'    : '%Y-%m-%d',
		'TIME_SERIES_WEEKLY'   : '%Y-%m-%d',
		'TIME_SERIES_MONTHLY'  : '%Y-%m-%d',
	}

	def __init__(self, ticker, time_series=TIME_SERIES['TIME_SERIES_DAILY']):
		self._ticker = ticker
		self._path = "../data/"
		self._filename = "d_{ticker}.csv".format(ticker=ticker.lower())
		self._time_series = time_series
		self._candles = {}
		self._candles_size = 0
		self._dates_idx = {}
		self._start_date = None
		self._pointer = None
		self._loadData()

	def _loadData(self):
		f = open(self._path + self._filename, "r")
		lines = f.readlines()[1:]
		count = 0

		for line in lines:
			slipted_line = line.split(",")
			self._dates_idx[slipted_line[0]] = count
			self._candles[count] = {
				'timestamp' : datetime.strptime(slipted_line[0], self._time_series),
				'open'      : round(eval(slipted_line[1]), 2),
				'high'      : round(eval(slipted_line[2]), 2),
				'low'       : round(eval(slipted_line[3]), 2),
				'close'     : round(eval(slipted_line[4]), 2),
				'volume'    : eval(slipted_line[5]),
			}
			count += 1

		self._candles_size = count
		self._pointer = count - 1
		self._start_date = self._candles[self._pointer]['timestamp']

	def getPrice(self):
		return self._candles[self._pointer]

	def setDatePoint(self, date):
		self._start_date = date
		self._pointer = self._dates_idx[self._start_date]

	def getNextPrice(self):
		self._pointer -= 1
		return self._candles[self._pointer]

	def hasNext(self):
		if self._pointer != 0:
			return True
		else:
			return False
