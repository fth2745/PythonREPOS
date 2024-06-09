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
from Data import *



anaYol = "https://fapi.binance.com/"

def fiyat(symbol,minute):
    url = f"https://fapi.binance.com/fapi/v1/klines?symbol={symbol}&interval={minute}&limit=500"
    
    payload={}
    headers={
        'Content-type':'application/json'
    }
    response=r.request('GET',url,headers=headers , data=payload).json()
    converted = pd.DataFrame(response, columns=["opentime", "open", "high", "low", "close", "volume", "closetime",
        "Quote asset volume", "Number of trades", "Taker buy base asset volume",
        "Taker buy quote asset volume", "ignore"], dtype=float)
    return fiyat
def zamanhesapla():
    ts = client.get_server_time()['serverTime']
    return ts

class Altcoin:
    def __init__(self,adet,coin,dakika,limit,tslYuzde,secret_key,api_key,leverage,marginType):
       self.adet =adet
       self.coin=coin
       self.dakika=dakika
       self.limit=limit
       self.tslYuzde=tslYuzde
       self.secret_key=secret_key
       self.api_key=api_key
       self.leverage=leverage
       self.marginType=marginType
   
    def marginKaldıraç(self):
        params={"symbol":self.koin,"leverage":self.leverage,"timestamp":zamanhesapla()}
        query_string = urlencode(params)
        params["signiture"]=hmac.new(secret_key.encode("UTF-8"),query_string.encode("UTF-8"),hashlib.sha256).hexdigest()
        url = urljoin(BASE_URL,"fapi/v1/leverage")
        payload={}
        headers={
        'Content-type':'application/json',
        'X-MBX-APIKEY': self.api_key
        }
        response=r.post(anaYol, headers=headers , params=params).json()
        return response
    
    def marginType(self):
        params = {
           "symbol":self.koin,
            "MarginType": self.marginType,
            "timestamp":zamanhesapla(),
    }
        query_string = urlencode(params)   
        params["signature"]=hmac.new(secret_key.encode("UTF-8"),query_string.encode("UTF-8"),hashlib.sha256).hexdigest()
        url = urljoin(BASE_URL,"fapi/v1/marginType")
        payload={}
        headers={
        'Content-type':'application/json',
        'X-MBX-APIKEY': self.api_key,
    }
        response=r.post(url, headers=headers , params=params).json()
        return response
     
    def islem(self):
        params ={"symbol":self.koin,     
            
            "timestamp":zamanhesapla(),}
        query_string = urlencode(params)   
        params["signature"]=hmac.new(secret_key.encode("UTF-8"),query_string.encode("UTF-8"),hashlib.sha256).hexdigest()
        url = urljoin(BASE_URL, "fapi/v2/positionRisk")
        payload={}
        headers={
        'Content-type':'application/json',
        'X-MBX-APIKEY': self.api_key,
    }
        response=r.get(url, headers=headers , params=params).json()
        verix =pd.DataFrame(response)
        return verix
    
    def islemdeMi(self):
        bilge = self.islem()["entryPrice"][0]
        if bilge>0:
            return True
        else:
            return False
    
    def emirGonder(self,pozisyon,tip):
     params = {
        "symbol" : self.koin , "side" : pozisyon , "type" : tip , "quantity" : self.adet , 
        "workingType" : "CONTRACT_PRICE", "timestamp" : zamanhesapla(), "positionSide" : "BOTH",
        "callbackRate":self.tslYuzde
    }
     query_string = urlencode(params)   
     params["signature"]=hmac.new(secret_key.encode("UTF-8"),query_string.encode("UTF-8"),hashlib.sha256).hexdigest()
     url = urljoin(BASE_URL,"fapi/v1/order")
     payload={}
     headers={
        'Content-type':'application/json',
        'X-MBX-APIKEY': self.api_key,
    }
     response=r.post(url, headers=headers , params=params).json()
     return response
   
    def kapat(self,pozisyon):
        if pozisyon =="long":
            self.emirGonder("SELL","MARKET")
        elif pozisyon == "short":
            self.emirGonder("BUY","MARKET")
            
    def longAc(self):
        self.emirGonder("BUY","MARKET")
    
    def shortAc(self):
        self.emirGonder("SELL","MARKET"),
        
    def gecmis(self):
     params = {"symbol": self.koin,"incomeType": "REALİZED_PNL","limit":10,"timestamp":zamanhesapla()}
     query_string = urlencode(params)   
     params["signature"]=hmac.new(secret_key.encode("UTF-8"),query_string.encode("UTF-8"),hashlib.sha256).hexdigest()
     url = urljoin(BASE_URL,"fapi/v1/incone")
     payload={}
     headers={
        'Content-type':'application/json',
        'X-MBX-APIKEY': self.api_key,
    }
     response=r.get(url, headers=headers , params=params).json()
     veri =pd.DataFrame(response,dtype=float)
     return veri
    
    def karHesapla(self):
        kar=0
        for sayac in range(0,5):
            kar += self.gecmiş()["income"][sayac]
        return f"son 5 işlemde toplam kar : {kar}"
    
    def tsl(self,pozisyon):
        if pozisyon == "long":
            self.emirGonder("SELL","TRAILING_STOP_MARKET")
        elif pozisyon=="short":
            self.emirGonder("BUY","TRAILING_STOP_MARKET")
   
    def emirGonder(self,pozisyon,tip):
     params = {
        "symbol" : self.koin , "timestamp" : zamanhesapla(), 
    }
     query_string = urlencode(params)   
     params["signature"]=hmac.new(secret_key.encode("UTF-8"),query_string.encode("UTF-8"),hashlib.sha256).hexdigest()
     url = urljoin(BASE_URL,"fapi/v1/allOpenOrders")
     payload={}
     headers={
        'Content-type':'application/json',
        'X-MBX-APIKEY': self.api_key,
        self.api_key:
            self.secret_key
    }
     response=r.post(url, headers=headers , params=params).json()
     return response   
 
    def acikEmirler(self):
     params={"symbol": self.koin,"timestamp":zamanhesapla()}
     query_string = urlencode(params)   
     params["signature"]=hmac.new(secret_key.encode("UTF-8"),query_string.encode("UTF-8"),hashlib.sha256).hexdigest()
     url = urljoin(BASE_URL,"fapi/v1/openOrders")
     payload={}
     headers={
        'Content-type':'application/json',
        'X-MBX-APIKEY': self.api_key,
        self.api_key:
            self.secret_key
    }
     response=r.get(url, headers=headers , params=params).json()
     veri =pd.DataFrame(response,dtype=float)
     return response   

        