# Reference https://www.alphavantage.co/documentation for settings

import requests
import datetime
import time
import ssl

class core_avapi():
    def __init__(self, api_token: str, symbol: str, interval='5min', adjusted='true', outputsize='compact', datatype='json'):
        self.api_token = api_token
        self.interval = interval
        self.symbol = symbol
        self.adjusted = adjusted
        self.outputsize = outputsize
        self.datatype = datatype
        self.last_request_data = ''
        self.convert_csv_to_json = False
        if datatype is 'json':
            self.convert_csv_to_json = True

    def get_intraday(self):
        url = f"https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={self.symbol}&interval={self.interval}&apikey={self.api_token}&outputsize={self.outputsize}&datatype={self.datatype}&adjusted={self.adjusted}"
        r = requests.get(url)
        if r.status_code == 200:
            data = r.json()
            self.last_request_data = data[f'Time Series ({self.interval})']
        else:
            print(f'ERROR!: {r.text}') # Convert to a an Exception

    def get_extended_intraday(self):
        pass

    def get_daily(self):
        pass

    def get_daily_adjusted(self):
        pass

    def get_weekly(self):
        pass

    def get_weekly_adjusted(self):
        pass

    def get_monthly(self):
        pass

    def get_monthly_adjusted(self):
        pass

    def get_quote_endpoint(self):
        pass

class fundamental_data():
    def __init__(self):
        pass

    def get_company_overview(self):
        pass

    def get_income_statement(self):
        pass

    def get_balance_sheet(self):
        pass

    def get_cash_flow(self):
        pass

    def get_earnings(self):
        pass

    def get_listing_and_delisting_status(self):
        pass

    def get_earnings_calendar(self):
        pass

    def get_ipo_calendar(self):
        pass

class forex():
    def __init__(self):
        pass

    def get_fx_exchange_rates(self):
        pass

    def get_fx_intraday(self):
        pass

    def get_fx_daily(self):
        pass

    def get_fx_weekly(self):
        pass

    def get_fx_monthly(self):
        pass

class cryptocurrencies():
    def __init__(self):
        pass

    def get_exchange_rates(self):
        pass

    def get_intraday(self):
        pass

    def get_daily(self):
        pass

    def get_weekly(self):
        pass

    def get_monethly(self):
        pass

class commodities():
    def __init__(self):
        pass

    def get_curde_oil_wti(self):
        pass

    def get_curde_oil_brent(self):
        pass

    def get_natural_gas(self):
        pass

    def get_copper(self):
        pass

    def get_aluminum(self):
        pass

    def get_wheat(self):
        pass

    def get_corn(self):
        pass

    def get_cotton(self):
        pass

    def get_sugar(self):
        pass

    def get_coffee(self):
        pass

    def get_global_commodities(self):
        pass

    def get_index(self):
        pass

class economic_indicators():
    def __init__(self):
        pass

    def get_real_gdp(self):
        pass

    def get_real_gdp_per_capita(self):
        pass

    def get_treasury_yield(self):
        pass

    def get_federal_funds_interest(self):
        pass

    def get_rate(self):
        pass

    def get_cpi(self):
        pass

    def get_inflation(self):
        pass

    def get_retail_sales(self):
        pass

    def get_durable_goods_orders(self):
        pass

    def get_unemployment_rate(self):
        pass

    def get_nonfarm_payroll(self):
        pass

class technical_indicators():
    def __init__(self):
        pass

    def get_sma(self):
        pass

    def get_ema(self):
        pass

    def get_wma(self):
        pass

    def get_dema(self):
        pass

    def get_tema(self):
        pass

    def get_trima(self):
        pass

    def get_kama(self):
        pass

    def get_mama(self):
        pass
    
    def get_vwap(self):
        pass

    def get_t3(self):
        pass

    def get_macd(self):
        pass

    def get_macdext(self):
        pass

    def get_stoch(self):
        pass

    def get_stochf(self):
        pass

    def get_rsi(self):
        pass

    def get_stochrsi(self):
        pass

    def get_willr(self):
        pass

    def get_adx(self):
        pass

    def get_apo(self):
        pass

    def get_ppo(self):
        pass

    def get_mom(self):
        pass

    def get_bop(self):
        pass

    def get_cci(self):
        pass

    def get_cmo(self):
        pass

    def get_roc(self):
        pass

    def get_rocr(self):
        pass

    def get_aroon(self):
        pass

    def get_aroonosc(self):
        pass

    def get_mfi(self):
        pass

    def get_trix(self):
        pass

    def get_ultosc(self):
        pass

    def get_dx(self):
        pass

    def get_minus_di(self):
        pass

    def get_plus_di(self):
        pass

    def get_minus_dm(self):
        pass

    def get_plus_dm(self):
        pass

    def get_bbands(self):
        pass

    def get_midpoint(self):
        pass

    def get_midprice(self):
        pass

    def get_sar(self):
        pass

    def get_trange(self):
        pass

    def get_atr(self):
        pass

    def get_natr(self):
        pass

    def get_ad(self):
        pass

    def get_obv(self):
        pass

    def get_ht_trendline(self):
        pass

    def get_ht_sine(self):
        pass

    def get_ht_trendmode(self):
        pass

    def get_ht_dcperiod(self):
        pass

    def get_ht_dcphase(self):
        pass

    def get_ht_phasor(self):
        pass
