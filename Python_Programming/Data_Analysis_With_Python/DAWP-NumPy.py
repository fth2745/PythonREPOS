##############################################################
# Python İle Veri Analizi
##############################################################

#-NumPy
#-Pandas
#-Veri Görselleştirme : Matplotlib & Seaborn
#-Gelişmiş Fonksiyonel Keşifçi Veri Analizi 


##############################################################
# NUMPY
########################################################################################
# 1-Numpy Giriş

#-Numpy Array'i Oluşturmak
#-Numpy Array Özellikleri
#-Yeniden Şekillendirme
#-Index Seçimi
#-Slicing
#-Fancy Index
#-Numpy'da Koşullu İşlemler
#-Numpy matematiksel işlemler


##############################################################
# Numpy Array'i Oluşturmak
##############################################################
import numpy as np

"""np.array([1,2,3,4,5])
type(np.array([1,2,3,4,5]))
np.zeros(10,dtype=int)
np.random.randint(0,10,size=10)
np.random.normal(10,4,(3,4))"""
##############################################################
# Numpy Array Özellikleri
##############################################################

"""a=np.random.randint(0,10,size=10)
print(a.ndim) #.ndim : Boyut Sayısı
print(a.shape) #.shape : Boyut Bİlgisi
print(a.size) #.size : toplam eleman sayısı
print(a.dtype) #.dtype:array veri tipi"""

##############################################################
# Reshape (Yeniden Şekillendirme)
##############################################################

"""a=np.random.randint(0,10,size=9).reshape(3,3)
print(a)"""

##############################################################
#Index Seçimi
##############################################################
"""a=np.random.randint(0,10,size=9).reshape(3,3)
print(a[:])
print(a[1,2])"""
##############################################################
#Fancy Index :Birden çok arrayin kontrolünü sağlar
##############################################################
"""V=np.arange(0,30,3)
catch=[1,2,3,4,5,6]

print(V[catch])
"""
##############################################################
# Numpy'da Koşullu İşlemler :array içinden koşullu eleman seçmemizi sağlar
##############################################################
"""v=np.random.randint(10,size=10)
print(v<3)
print(v[v!=3])"""
##############################################################
#Matematiksel işlemler
##############################################################
"""v=np.array([1,2,3,4,5,6,7,8,9])
np.subtract(v,1)
np.add(v,1)
np.mean(v)
np.sum(v)
np.min(v)
np.max(v)
np.var(v)

#2 bilinmeyenli denklem
a= np.array([[5,1],[1,3]])
b=np.array([12,10])
c=np.linalg.solve(a,b)
print(c)"""





