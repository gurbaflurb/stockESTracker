#!/usr/bin/python

import argparse
import requests
import datetime
import time
import ssl

from dotenv import dotenv_values
from elasticsearch import Elasticsearch

def send_elastic_data(es_doc, es_host, es_user, es_password):
    ssl_context = ssl.create_default_context()
    ssl_context.check_hostname=False
    es = Elasticsearch(hosts=[es_host],
        basic_auth=(es_user, es_password),
        ssl_context=ssl_context,
        verify_certs=False
    )
    print(f'Sending document: {es_doc}')
    es.index(
        index='stocks',
        document=es_doc
    )
    es.indices.refresh(index='stocks')

def get_stock_history(stock, API_KEY):
    url = f"https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={stock}&interval=1min&apikey={API_KEY}&datatype=json&outputsize=full"
    r = requests.get(url)
    if r.status_code == 200:
        data = r.json()
        print(data)
        return data['Time Series (1min)']
    else:
        print(f'ERROR!: {r.text}')
        
def convert_timestamp(orig_timestamp):
    dt_object = datetime.datetime.strptime(orig_timestamp, "%Y-%m-%d %H:%M:%S")
    epoch_time = dt_object.isoformat()
    return epoch_time

def convert_to_es_and_send(stock_history, stock, es_host, es_user, es_password):
    for i in stock_history:
        doc = {}
        doc['timestamp'] = convert_timestamp(i)
        doc['open'] = float(stock_history[i]['1. open'])
        doc['high'] = float(stock_history[i]['2. high'])
        doc['low'] = float(stock_history[i]['3. low'])
        doc['close'] = float(stock_history[i]['4. close'])
        doc['volume'] = float(stock_history[i]['5. volume'])
        doc['stock_index'] = stock
        
        send_elastic_data(doc, es_host, es_user, es_password)

def main(args):
    ENVIRONMENT = dotenv_values(".env")
    API_KEY = ENVIRONMENT['API_KEY']
    STOCKS = ENVIRONMENT['STOCKS'].split(',')

    for stock in STOCKS:
        stock_data = get_stock_history(stock, API_KEY)
        import pprint
        pprint.pprint(stock_data)
        #convert_to_es_and_send(stock_data, stock, ENVIRONMENT['ES_HOST'], ENVIRONMENT['ES_USER'], ENVIRONMENT['ES_PASSWORD'])
        #time.sleep(30)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--interactive', dest='interactive', type=bool, default=False, help='Run The stock tracer in interactive mode')
    parser.add_argument('-d', '--daemon', dest='daemon', type=bool, default=False, help='Run The stock tracer in daemon(detached) mode')
    args = parser.parse_args()
    main(args)
