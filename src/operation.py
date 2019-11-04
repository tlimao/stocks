class Operation:

    BUY = 'buy'
    SELL = 'sell'
    NEUTRAL = 'neutral'

    def __init__(self, operation_type, ticker, price, qnt):
        self._type   = operation_type
        self._ticker = ticker
        self._price  = price
        self._qnt    = qnt

        self._str = "[{ticker} | {qnt} | {price} | {type}]"

    def __str__(self):
        return self._str.format(ticker=self._ticker, qnt=self._qnt, price=self._price, type=self._type)

    def getOperationData(self):
        operation =  {
            'ticker' : self._ticker,
            'qnt'    : self._qnt,
            'price'  : self._price,
            'type'   : self._type,
        }

        return operation
