# -Dictionary

# -Sırasız (3.7 den sonra sıralı)
# -Değiştirilebilir
# -Kapsayıcıdır


# -{"key":value,} şeklinde yaızlır

dict={"Fatih":"Bilge"}
print(dict)

#Fatih keyine ait değeri getirir
print(dict["Fatih"])

#Fatih keyine ait değeri değiştirir
dict["Fatih"]="Bilgili"
print(dict)

#Yeni bir key-value çifti ekler
dict["Ahmet"]="Kaya" 
print(dict)

#Sözlükteki tüm elemanları sil
dict.clear()

#Fatih keyine ait değeri getirir
print(dict.get("Fatih")) 

#Mehmet keyine ait değeri getirir, eğer yoksa None döner
print(dict.get("Mehmet")) 

#Sözlükteki tüm keyleri getirir
print(dict.keys()) 

#Sözlükteki tüm value leri getirir
print(dict.values())

#Sözlükteki tüm key-value çiftlerini getirir
print(dict.items()) 

#Fatih keyine ait değeri siler
dict.pop("Fatih") 
print(dict)

#Son eklenen key-value çiftini siler
dict.popitem() 
print(dict)

#Sözlükteki tüm elemanları günceller
dict.update({"Fatih":"Bilgili","Ahmet":"Kaya"})
dict.update({"Mehmet":"Kaya"})
print(dict)

#Fatih keyine ait değeri getirir, eğer yoksa "Bilgili" değ
dict.setdefault("Fatih","Bilgili")
print(dict)

#Mehmet keyine ait değeri getirir, eğer yoksa "Kaya" değ
dict.setdefault("Mehmet","Kaya") 
print(dict)

#Yeni bir sözlük oluştur
dict.fromkeys(["Fatih","Ahmet","Mehmet"],"Bilgili") 
print(dict)

#Sözlüğün kopyasını oluşturur
dict.copy() 
print(dict)

#Fatih keyine ait değeri getirir, eğer yoksa "Bilgili" değ
dict.setdefault("Fatih","Bilgili")

#Mehmet keyine ait değeri getirir, eğer yoksa "Kaya" değ
dict.setdefault("Mehmet","Kaya")
print(dict)

#Son eklenen key-value çiftini siler
dict.popitem() 
print(dict)

#Fatih keyine ait değeri siler
dict.pop("Fatih") 
print(dict)

 #Sözlükteki tüm elemanları siler
dict.clear()
print(dict)


