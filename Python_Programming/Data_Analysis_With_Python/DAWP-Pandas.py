#############################################
# PANDAS
import pandas as pd
import numpy as np
import seaborn as se

#############################################


# Pandas Series
# Veri Okuma
# Veriye Hızlı Bir Bakış
# Pandasta seçim işlemleri
# Toplulaştırma ve Gruplama
# Apply ve Lambda 
# Birleştirme (JOin)

#########################################################
# Pandas Series
"""s= pd.Series([10,20,13,30])
print(s.head(3))
s.index # index bilglierni verir
s.dtype 
s.size
s.ndim 
s.values
s.head(3)#ilk 3 verinin index ve value değerlerini verir
s.tail(3)#son 3 verinin index ve value değerlerini verir"""
#########################################################
# Veri Okuma
"""df = pd.read_csv("Python_Programming\Data_Analysis_With_Python\Advertising.csv")
print(df.head())
print(df.columns)
print(df.sort_index)"""
#########################################################
# Veriye Hızlı Bir Bakış
"""df=se.load_dataset("titanic")
print(df.tail())
print(df.head())
print(df.shape)
print(df.head())    
print(df.info())
print(df.describe().T)# veri setindeki sayısal değişkenleri verir
print(df.isnull().values.any()) # Özetle, bu ifade DataFrame'de herhangi bir eksik değer olup olmadığını kontrol eder ve sonucu ekrana yazdırır.
print(df.isnull().sum()) #  Bu kod, her bir sütundaki eksik değer sayılarını ekrana yazdırır. Bu sayede, her sütunda kaç tane eksik değer olduğunu görebilirsiniz.
print(df["sex"].head()) #"sex" sütününn ilk 5 değerini getirir
print(df["sex"].value_counts()) # sex sütünundaki değişkenlerin kaçar defa kullanıldığını gösterir
print(df["age"].mean()) # age sütünundaki ortalama değeri gösterir
print(df["age"].median()) # age sütünundaki medyan değeri gösterir
print(df["age"].mode()) # age sütünundaki moda değeri gösterir
print(df["age"].std()) # age sütünundaki standart sapma değeri gösterir
print(df["age"].var()) # age sütünundaki varyans değeri gösterir"""
#########################################################
# Pandasta seçim işlemleri
df=se.load_dataset("titanic")
df[0:13]
df.drop(0,axis=0)
delete_indexes=[1,3,5,7]
print(df.drop(delete_indexes,axis=0).head())
df.drop(delete_indexes,axis=0,inplace=True).head()#herhangi bir değere atamadan kalıcı hale getirri "inplace=True"






