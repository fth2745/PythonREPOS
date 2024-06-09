import time
import requests
import talib.stream
from Veri import Altcoin,fiyat,binance
from fonksiyonlar import yukarıKes,asagiKes,bekle
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




api_key=input("Api key giriniz :: ")
secret_key=input("Secret Key giriniz  ::")
koin=input("Hangi Kodu giriniz")
adet=float(input("kaç adet alınacak"))
dakika=input("Periyot giriniz")
limit = 0
price = fiyat(koin,dakika)["close"][len(fiyat(koin,dakika)["close"])-1]
print(koin,"fiyatı ::",price)


secim = input("Kar al ve Stoplu bi strateji mi olsun Y/N")
if secim == "Y":
    tslYuzde=float(input("İz süren stop yüzdesi gir  ::"))
    stop = float(input("kaç dolar zararda stop istersin ::"))
    kar = float(input("Kaç dolarda işlemi kapatmak istiyosun ::"))
    tezdAktif= float(input("Takip eden Zarar Durdur PNL kaç oldukatn sonra çalışsın ::"))
else:
    tslYuzde=0
    kaldirac = input("kaç X kaldıraç:")
    marginType="İSOLATED"

koin1 = Altcoin(adet,koin,dakika,limit,tslYuzde,secret_key,api_key,kaldirac,marginType)
bekle(1)
koin1.marginType()
bekle(1)
koin1.marginKaldıraç()
bekle(1)


def emaKesisim():#Ema kesişimlerine göre işleme giren strateji
    emaKisa = input("Kısa ema girin ::")
    emaUzun = input("Uzun ema girin")
    izAktif = False

    islemTipi =""
    while True:
      close = koin1.bilgisel()["close"] #kapanış değerini getirir
      bekle(1)
      islem=koin1.islem()
      profit = islem["unRealizedProfit"][0]
      bekle(1)
      pnl=float(profit)
      emaK =talib.EMA(close,float(emaKisa))
      emaU= talib.EMA(close,float(emaUzun))
      kontrol =islem["entryPrice"][0]
      bekle(1)
      if float(kontrol) <= 0 :
          koin1.emiriptal()
          bekle(1)
          izAktif=False
          bekle(1)
          if yukarıKes(emaK,emaU) is True :
              koin1.longAc()
              islemTipi="Long"
              bekle(1)
              giris = koin1.islem()["entryPrice"][0]
              bekle(1)
              print(f"{koin1,koin1}{giris}fiyatından  Long açıldı")
          elif asagiKes(emaK,emaU)  is True:
              koin.shortAc()
              işlemTipi = "Short"
              bekle(1) 
              giris = koin1.islem()["entryPrice"][0]
              bekle(1)
              print(f"{koin1,koin1}{giris}fiyatından  Short açıldı")
      elif float(kontrol) >0:
          if islemTipi=="long":
            if asagiKes(emaK,emaU) is True:
                koin1.kapat(islemTipi)
                islemTipi="short"
                bekle(1)
                giris = koin1.islem()["entryPrice"][0]
                bekle(1)
                print(f"{koin1,koin1}{giris}fiyatından Long işlem kapatılıp Short açıldı")
            elif secim =="Y":
                if pnl > kar : 
                    koin1.kapat(islemTipi)
                    islemTipi= ""
                    print("kar alındı")
                elif pnl < -stop:
                    koin1.kapat(islemTipi)
                    islemTipi=""
                    print("Stop olundu")
                elif pnl > tezdAktif and izAktif is False:
                    koin1.tsl(islemTipi)
                    print("iz süren Stop aktifleştirildi")
                    izAktif = True
          elif  islemTipi == "short":
              if yukarıKes(emaK,emaU) is True:
                  koin1.kapat(islemTipi) 
                  koin1.longAc()
                  işlemTipi="Long"
                  bekle(1)
                  giris = koin1.islem()["entryPrice"][0]
                  bekle(1)
                  print(f"{koin1.koin1}{giris}fiyatından Short işlem kapatılıp Long işlem açıldı")    
              elif secim =="Y":
                if pnl > kar : 
                    koin1.kapat(islemTipi)
                    islemTipi= ""
                    print("kar alındı")
                elif pnl < -stop:
                    koin1.kapat(islemTipi)
                    islemTipi=""
                    print("Stop olundu")
                elif pnl > tezdAktif and izAktif is False:
                    koin1.tsl(islemTipi)
                    print("iz süren Stop aktifleştirildi")
                    izAktif = True       
                    
    
strateji_secim = input("1 -- EMA Kesişimlerine göre işlem açar ::::  2 -- SMA Kesişimlerine göre işlem açar ::::  Seçim ?")
if strateji_secim == 1:
    emaKesisim()
else :
    print("Strateji seçmediniz")


