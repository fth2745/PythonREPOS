# -Set

#- Değiştirilebilir
#- Sırasız + eşsizdir
#- Kümelerde işlem sırası yoktur   
#- kapsaycıdır


set1=set([1,2,3])
set2=set([1,4,5])
# -instersection():Ortak olanları yazdırı
print(set1.intersection(set2)) # 1
#- union():iki Küme birleşimi
print(set1.union(set2)) # 1,2,3,4,5

#- difference():Kümlerein farkları
print(set1.difference(set2)) # 2,3
#- symmetric_difference():İkisinin birbiriyle farkları
print(set1.symmetric_difference(set2)) # 2,3,4,5
#- issubset()
print(set1.issubset(set2)) # False
#- issuperset()
print(set1.issuperset(set2)) # False
#- add() : Ekleme yapar
set1.add(6)
print(set1) # 1,2,3,6
#- remove() : Çıkarma yapar
set1.remove(6)
print(set1) # 1,2,3
#- discard() : Çıkarma yapar
set1.discard(6)
print(set1) # 1,2,3
#- clear() : Tüm elemanları siler
set1.clear()



