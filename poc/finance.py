import datetime as dt
import os
import pprint

import yfinance as yf

import config as fconfig


class FinanceApp:
    def __init__(self, config):
        self._config = config
        tickers = config.get('track')
        symbols = [ticker.get('symbol') for ticker in tickers]
        self._symbols = {symbol: _Ticker(symbol) for symbol in symbols}
        
    def display_all(self):
        for ticker in self._symbols.values():
            ticker.display()
            

class _Ticker:
    def __init__(self, symbol):
        self._symbol = symbol
        self._info = yf.Ticker(symbol).info
        self._numbers = {k:v for k, v in self._info.items() if isinstance(v, (int, float))}

    @property
    def current_price(self):
        return self._info.get('currentPrice')
    
    @property
    def day_high(self):
        return self._info.get('dayHigh')
    
    @property
    def day_low(self):
        return self._info.get('dayLow')
        
    @property
    def dividend_rate(self):
        return self._info.get('dividendRate')

    @property
    def ex_dividend_date(self):
        epoch = self._info.get('exDividendDate')
        return dt.datetime.fromtimestamp(epoch).isoformat() if epoch else ''
        
    @property
    def fifty_day_average(self):
        return self._info.get('fiftyDayAverage')
    
    @property
    def fifty_two_week_high(self):
        return self._info.get('fiftyTwoWeekHigh')
    
    @property
    def fifty_two_week_low(self):
        return self._info.get('fiftyTwoWeekLow')
        
    @property
    def numbers(self):
        return self._numbers
    
    @property
    def open(self):
        return self._info.get('open')
    
    @property
    def target_low_price(self):
        return self._info.get('targetLowPrice')
    
    @property
    def target_mean_price(self):
        return self._info.get('targetMeanPrice')
    
    @property
    def target_high_price(self):
        return self._info.get('targetHighPrice')
    
    def display(self):
        print(self._symbol)
        pprint.pprint(self.to_dict())
        
    def to_dict(self):
        return {
            'symbol': self._symbol,
            'currentPrice': self.current_price,
            'dayHigh': self.day_high,
            'dayLow': self.day_low,
            'dividendRate': self.dividend_rate,
            'exDividendDate': self.ex_dividend_date,
            'fiftyDayAverage': self.fifty_day_average,
            'fiftyTwoWeekHigh': self.fifty_two_week_high,
            'fiftyTwoWeekLow': self.fifty_two_week_low,
            'open': self.open,
            'targetLow': self.target_low_price,
            'targetMean': self.target_mean_price,
            'targetHigh': self.target_high_price,
        }


def main():
    config_file = os.path.join(os.path.dirname(__file__), 'config.json')
    config = fconfig.Config(config_file)
    app = FinanceApp(config)
    app.display_all()
    

if __name__ == '__main__':
    main()