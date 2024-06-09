import pandas as pd
import json 
import urllib as ul
import requests as r
import urllib.request as uls
from urllib.parse import urljoin,urlencode
import talib.stream
import time
import hmac
import hashlib
from binance import Client
from datetime import datetime


api_key= "MeW9iufwGNsVvvVaZNNREqxbBZOxqqHYt1yaX48ltvp9SGArYJCcNRLeWTJTYuAH"
secret_key = "h1UIthWmU7wrQsaB35IphnIK2NuZZOZD4wTZE0H6FzHrdhL05zKQzXwi1E2EgnPz"
BASE_URL = "https://fapi.binance.com/"
client = Client(api_key,secret_key)


 
def position_info():
    params = {
        "symbol": "BTCUSDT",
        "timestamp" : timestamp()
    }
    query_string = urlencode(params)
    params["signature"] = hmac.new(secret_key.encode("UTF-8"), query_string.encode("UTF-8"), hashlib.sha256).hexdigest()
    url = urljoin(BASE_URL, "fapi/v2/positionRisk")
    headers = {
        'Content-type': 'application/json',
        'X-MBX-APIKEY': api_key,
    }
    response = pd.DataFrame(r.get(url, headers=headers, params=params).json())
    return response

def hikayede_fonksiyon():
    params = {
           "symbol":"BTCUSDT",
            "interval":"15m",
            'limit':"10",
            "timestamp":timestamp()
    }
    query_string = urlencode(params)
    params["signiture"]=hmac.new(secret_key.encode("UTF-8"),query_string.encode("UTF-8"),hashlib.sha256).hexdigest()
    url = urljoin(BASE_URL,"fapi/v1/klines")
    payload={}
    headers={
        'Content-type':'application/json',
        'X-MBX-APIKEY': api_key,
    }
    response=r.request('GET',url,headers=headers , params=params).json()
    data = pd.DataFrame(response,)
    return data
    
def get_all_symbols():
    response = uls.urlopen(f"{BASE_URL}fapi/v1/exchangeInfo").read()
    return list(map(lambda symbol: symbol['symbol'], json.loads(response)['symbols']))

def get_data_symbols(symbol_name,period,limit):
    params = {
           "symbol":symbol_name,
            "interval":period,
            'limit':limit
    }
    query_string = urlencode(params)   
    url = urljoin(BASE_URL,"fapi/v1/klines")
    payload={}
    headers={
        'Content-type':'application/json'
    }
    response=r.request('GET',url,headers=headers , params=params).json()
    converted = pd.DataFrame(response, columns=["opentime", "open", "high", "low", "close", "volume", "closetime",
        "Quote asset volume", "Number of trades", "Taker buy base asset volume",
        "Taker buy quote asset volume", "ignore"], dtype=float)
    return converted

def get_buy_sell_volume(symbol_name, period, limit):
    params = {
        "symbol": symbol_name,
        "period": period,
        "limit": limit
    }
    query_string = urlencode(params)
    url = urljoin(BASE_URL, "futures/data/takerlongshortRatio")
    payload={}
    headers = {"Content-type": "application/json"}
    response = r.request("GET", url, headers=headers, params=params)
    data = response.json()
    return data

def marginType():
    params = {
           "symbol":"BTCUSDT",
            "MarginType": "ISOLATED",
            "timestamp":timestamp()
    }
    query_string = urlencode(params)   
    params["signature"]=hmac.new(secret_key.encode("UTF-8"),query_string.encode("UTF-8"),hashlib.sha256).hexdigest()
    url = urljoin(BASE_URL,"fapi/v1/marginType")
    payload={}
    headers={
        'Content-type':'application/json',
        'X-MBX-APIKEY': api_key,
    }
    response=r.post(url, headers=headers , params=params).json()
    return response

def leverage():
    params = {
        "symbol" : "BTCUSDT" , "leverage" : "10", "timestamp" : timestamp()
    }
    query_string = urlencode(params)   
    params["signature"]=hmac.new(secret_key.encode("UTF-8"),query_string.encode("UTF-8"),hashlib.sha256).hexdigest()
    url = urljoin(BASE_URL,"fapi/v1/leverage")
    payload={}
    headers={
        'Content-type':'application/json',
        'X-MBX-APIKEY': api_key,
    }
    response=r.post(url, headers=headers , params=params).json()
    return response

def emirver():
    params = {
        "symbol" : "BTCUSDT" , "side" : "BUY" , "type" : "MARKET" , "quantity" : 20 , 
        "workingType" : "CONTRACT_PRICE", "timestamp" : timestamp(), "positionSide" : "BOTH"
    }
    query_string = urlencode(params)   
    params["signature"]=hmac.new(secret_key.encode("UTF-8"),query_string.encode("UTF-8"),hashlib.sha256).hexdigest()
    url = urljoin(BASE_URL,"fapi/v1/order")
    payload={}
    headers={
        'Content-type':'application/json',
        'X-MBX-APIKEY': api_key,
    }
    response=r.post(url, headers=headers , params=params).json()
    return response

def timestamp():
    ts = client.get_server_time()['serverTime']
    return ts



