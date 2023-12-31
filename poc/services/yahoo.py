import datetime as dt

class _StockInfo:
    def __init__(self, stock_data):
        self._stock_data = stock_data
        
    @property
    def current_price(self):
        return self._stock_data.get('currentPrice')
    
    @property
    def day_high(self):
        return self._stock_data.get('dayHigh')
    
    @property
    def day_low(self):
        return self._stock_data.get('dayLow')
    
    @property
    def dividend_rate(self):
        return self._stock_data.get('dividendRate')
    
    @property
    def ex_dividend_date(self):
        epoch = self._stock_data.get('exDividendDate')
        return dt.datetime.fromtimestamp(epoch).isoformat() if epoch else ''
    
    @property
    def fifty_day_average(self):
        return self._stock_data.get('fiftyDayAverage')
    
    @property
    def fifty_two_week_high(self):
        return self._stock_data.get('fiftyTwoWeekHigh')

    @property
    def fifty_two_week_low(self):
        return self._stock_data.get('fiftyTwoWeekLow')