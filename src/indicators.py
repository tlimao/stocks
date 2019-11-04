class Rsi:

    def __init__(self, days=5):
        self._N = days
        self._U = 0
        self._D = 0

        self._rsi = 0
        self._last_price = 0

        self._U_array = [0 for i in range(days)]
        self._D_array = [0 for i in range(days)]

    def getRsi(self):
        return self._rsi

    def update(self, value):
        if value > self._last_price:
            self._U_array = self._U_array[1:]
            self._U_array.append(value)
        else:
            self._D_array = self._D_array[1:]
            self._D_array.append(value)
        
        self._last_price = value
        
        self._U = sum(self._U_array)
        self._D = sum(self._D_array)

        self._rsi = round(100.00 - (100.00/(1.00 + self._U/self._D)), 0)