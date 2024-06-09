from Veri import *
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



def bekle(sn):
 time.sleep(sn)

def yukarıKes(a,b):
    oncekiKisa = a[len(a)-3]
    kisa = a[len(a)-2]
    simdikisa = a[len(a)-1]
    
    oncekiUzun = a[len(b)-3]
    Uzun = a[len(b)-2]
    simdiuzun = a[len(b)-1]
    if oncekiKisa<oncekiUzun and kisa > Uzun and simdikisa > simdiuzun:
        return True
    else:
        return False
    
def dipMi(a):
     ikiOnce= a[len(a)-3]
     birOnce= a[len(a)-2]
     once= a[len(a)-1]
     if ikiOnce > birOnce and once > birOnce:
         return True
     else: 
          return False
def tepeMi(a):
    ikiOnce= a[len(a)-3]
    birOnce= a[len(a)-2]
    once= a[len(a)-1]
    if ikiOnce < birOnce and once < birOnce:
         return True
    else: 
          return False
def asagiKes(a,b):
    oncekiKisa = a[len(a)-3]
    kisa = a[len(a)-2]
    simdikisa = a[len(a)-1]
    oncekiUzun = a[len(b)-3]
    Uzun = a[len(b)-2]
    simdiuzun = a[len(b)-1]
    if oncekiKisa> oncekiUzun and kisa < Uzun and simdikisa < simdiuzun:
        return True
    else:
        return False
    
def retestUp(a,b):
    k3=a[len(a)-4]
    k2=a[len(a)-3]
    k1=a[len(a)-2]
    k0=a[len(a)-1]
    u3=b[len(b)-4]
    u2=b[len(b)-3]
    u1=b[len(b)-2]
    u0=b[len(b)-1]
    if k3 > k2 and k2 < k1 < k0 and k2 < u2*1.0008 and k1 > u1*1.0008 and k0 > u0:
        return True
    else: 
        return False
    
def retesDown(a,b):
    k3=a[len(a)-4]
    k2=a[len(a)-3]
    k1=a[len(a)-2]
    k0=a[len(a)-1]
    u3=b[len(b)-4]
    u2=b[len(b)-3]
    u1=b[len(b)-2]
    u0=b[len(b)-1]
    if k3 < k2 and k2 > k1 > k0 and k2 > u2*1.0008 and k1 < u1*1.0008 and k0 > u0:
        return True
    else: 
        return False
    
def enYuksek(a,barSayisi):
    return max(a.tail(barSayisi))

def mesafe(l,el):
    for i in l.index:
        if l[i] == el:
            return len(l)-i-1
    return None

def enDusuk(a,barSayisi):
    return min(a.tail(barSayisi))

    
    