class Rsi:

    def __init__(self, days=5):
        self._N = days

        self._rsi = 0
        self._last_price = 0

        self._U_array = []
        self._D_array = []

        self._U_Av = 0
        self._D_Av = 0

    def getRsi(self):
        return self._rsi

    def update(self, value):
        u_Size = len(self._U_array)

        if u_Size < self._N:
            if value > self._last_price:
                self._U_array.append(value)
                self._D_array.append(0)
            else:
                self._U_array.append(0)
                self._D_array.append(value)

            self._last_price = value

            self._U_Av = sum(self._U_array)/(u_Size + 1)
            self._D_Av = sum(self._D_array)/(u_Size + 1)
        
        else:
            if value > self._last_price:
                self._U_Av = (self._U_Av * 13 + value)/14
                self._D_Av = (self._D_Av * 13 + 0)/14
            else:
                self._U_Av = (self._U_Av * 13 + 0)/14
                self._D_Av = (self._D_Av * 13 + value)/14

            self._last_price = value

            self._rsi = round(100.00 - (100.00/(1.00 + self._U_Av/self._D_Av)), 0)