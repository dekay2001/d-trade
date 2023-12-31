import pytest

from assertpy import assert_that

import poc.services.yahoo as service


class TestStockInfo:
    @pytest.fixture
    def stock_data(self):
        return {
            '52WeekChange': 0.0059295893,
            'SandP52WeekChange': 0.1422813,
            'ask': 113.7,
            'askSize': 1100,
            'auditRisk': 8,
            'averageDailyVolume10Day': 6382490,
            'averageVolume': 8603230,
            'averageVolume10days': 6382490,
            'beta': 1.088,
            'bid': 113.48,
            'bidSize': 900,
            'boardRisk': 10,
            'bookValue': 9.167,
            'compensationAsOfEpochDate': 1703980800,
            'compensationRisk': 2,
            'currentPrice': 113.48,
            'currentRatio': 2.866,
            'dateShortInterest': 1700006400,
            'dayHigh': 113.55,
            'dayLow': 109.75,
            'debtToEquity': 87.159,
            'dividendRate': 1.48,
            'dividendYield': 0.0134000005,
            'earningsGrowth': 0.011,
            'earningsQuarterlyGrowth': -0.012,
            'ebitda': 6709000192,
            'ebitdaMargins': 0.13035,
            'enterpriseToEbitda': 26.247,
            'enterpriseToRevenue': 3.421,
            'enterpriseValue': 176093364224,
            'exDividendDate': 1701388800,
            'fiftyDayAverage': 101.7304,
            'fiftyTwoWeekHigh': 131.31,
            'fiftyTwoWeekLow': 88.66,
            'firstTradeDateEpochUtc': 344615400,
            'fiveYearAvgDividendYield': 0.97,
            'floatShares': 1206387718,
            'forwardEps': 3.97,
            'forwardPE': 28.584383,
            'freeCashflow': 3749250048,
            'fullTimeEmployees': 83700,
            'gmtOffSetMilliseconds': -18000000,
            'governanceEpochDate': 1701129600,
            'grossMargins': 0.43515998,
            'heldPercentInsiders': 0.0139999995,
            'heldPercentInstitutions': 0.83726,
            'impliedSharesOutstanding': 1521910016,
            'lastDividendDate': 1693526400,
            'lastDividendValue': 0.34,
            'lastFiscalYearEnd': 1685491200,
            'lastSplitDate': 1450915200,
            'marketCap': 172706349056,
            'maxAge': 86400,
            'mostRecentQuarter': 1693440000,
            'netIncomeToCommon': 5052000256,
            'nextFiscalYearEnd': 1717113600,
            'numberOfAnalystOpinions': 33,
            'open': 110.33,
            'operatingCashflow': 5417999872,
            'operatingMargins': 0.12397,
            'overallRisk': 8,
            'payoutRatio': 0.41979998,
            'pegRatio': 2.46,
            'previousClose': 109.9,
            'priceHint': 2,
            'priceToBook': 12.379187,
            'priceToSalesTrailing12Months': 3.3555412,
            'profitMargins': 0.09816,
            'quickRatio': 1.6,
            'recommendationMean': 2.3,
            'regularMarketDayHigh': 113.55,
            'regularMarketDayLow': 109.75,
            'regularMarketOpen': 110.33,
            'regularMarketPreviousClose': 109.9,
            'regularMarketVolume': 7820381,
            'returnOnAssets': 0.09348,
            'returnOnEquity': 0.33914003,
            'revenueGrowth': 0.02,
            'revenuePerShare': 33.38,
            'shareHolderRightsRisk': 7,
            'sharesOutstanding': 1224009984,
            'sharesPercentSharesOut': 0.0113,
            'sharesShort': 17193517,
            'sharesShortPreviousMonthDate': 1697155200,
            'sharesShortPriorMonth': 18602014,
            'shortPercentOfFloat': 0.0174,
            'shortRatio': 2.04,
            'targetHighPrice': 136.69,
            'targetLowPrice': 80.19,
            'targetMeanPrice': 108.87,
            'targetMedianPrice': 110.26,
            'totalCash': 8789999616,
            'totalCashPerShare': 5.776,
            'totalDebt': 12177000448,
            'totalRevenue': 51469000704,
            'trailingAnnualDividendRate': 1.36,
            'trailingAnnualDividendYield': 0.012374886,
            'trailingEps': 3.24,
            'trailingPE': 35.024693,
            'trailingPegRatio': 2.0083,
            'twoHundredDayAverage': 110.14435,
            'volume': 7820381
        }
    
    @pytest.fixture
    def info(self, stock_data):
        return service._StockInfo(stock_data)

    def test_current_price(self, info):
        assert_that(info.current_price).is_equal_to(113.48)
        
    def test_day_high(self, info):
        assert_that(info.day_high).is_equal_to(113.55)
        
    def test_day_low(self, info):
        assert_that(info.day_low).is_equal_to(109.75)   
        
    def test_dividend_rate(self, info): 
        assert_that(info.dividend_rate).is_equal_to(1.48)
        
    def test_ex_dividend_date(self, info):
        assert_that(info.ex_dividend_date).is_equal_to('2023-11-30T19:00:00')  
        
    def test_ex_dividend_date_is_empty_string_when_epoch_is_none(self, stock_data):
        stock_data['exDividendDate'] = None
        info = service._StockInfo(stock_data)
        assert_that(info.ex_dividend_date).is_equal_to('') 
        
    def test_fifty_day_average(self, info): 
        assert_that(info.fifty_day_average).is_equal_to(101.7304)   
        
    def test_fifty_two_week_high(self, info):   
        assert_that(info.fifty_two_week_high).is_equal_to(131.31)
        
    def test_fifty_two_week_low(self, info):   
        assert_that(info.fifty_two_week_low).is_equal_to(88.66)     
    

if __name__ == '__main__':
    unittest.main()