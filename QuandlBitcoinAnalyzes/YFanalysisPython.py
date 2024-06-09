
import quandl
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import scale
import math, datetime

style.use("ggplot")

# Quandl API 
api_key = "vsZYB2Gkm3sqnwLi3ohN"
quandl.ApiConfig.api_key = api_key

# Bitcoin fiyat verilerini Quandl'dan alır
df = quandl.get('BITFINEx/BTCUSD')

# Eksik veriler temizlenir
df.dropna(inplace=True)

# Yüzde değişimleri ve oranları hesaplanır
df['HL_PCT'] = (df['High'] - df['Low']) / df['Last'] * 100.0
df['ASKBID_PCT'] = (df['Ask'] - df['Low']) / df['Ask'] * 100.0

# İlgili sütunları seçilir
df = df[['High','Low','Last','HL_PCT','ASKBID_PCT','Volume']]

# Tahmin yapılacak gün sayısını belirler
forecast_out = int(math.ceil(len(df) * 0.001))

# Fiyat sütununu belirtilen gün sayısı kadar kaydırarak "Label" adlı yeni bir sütun oluştur
df['Label'] = df['Last'].shift(-forecast_out+1)

# Giriş verilerini ölçeklendirir
x = scale(df.drop(columns='Label'))
y = df.iloc[:,-1]

# Tahmin yapılacak günler
x_toPredict = x[-forecast_out:]
x = x[:-forecast_out]
y = y[:-forecast_out]

# Eğitim ve test veri setleri
x_train, x_test, y_train, y_test = train_test_split(x, y, train_size=0.8, random_state=0)

# Lineer Regresyon modelini oluşturulur ve eğitilir
regressor = LinearRegression()
regressor.fit(x_train, y_train)

# Doğruluk hesaplama
accuracy = regressor.score(x_test, y_test)

# Tahmin
prediction_set = regressor.predict(x_toPredict)

# Tahminleri içeren sütunu ekleyerek yeni veri oluşturulur
df['Prediction'] = np.nan
last_date = df.iloc[-1].name
lastDatetime = last_date.timestamp()
one_day = 3600 * 24
nextDatetime = lastDatetime + one_day

onceki_veri = len(df)
for i in prediction_set:
    next_date = datetime.datetime.fromtimestamp(nextDatetime)
    nextDatetime += one_day
    df.loc[next_date] = [np.nan for q in range(len(df.columns) - 1 )] + [i]
    last_deger = df.iloc[-1,7]
    df.iloc[-1,2] = last_deger

# Tahmin ve gerçek fiyatları içeren sütunlar
df['Prediction'] = df['Last']
df.iloc[0:onceki_veri+1]['Last'].plot(color='b')
df.iloc[onceki_veri:len(df)+1]['Prediction'].plot(color='r')

# Grafik detayları
plt.title(f"Doğruluk : {accuracy :.2f}")
plt.xlabel('Tarih')
plt.ylabel('USD(Fiyat)')
plt.legend(loc=4)
plt.show()
