# -List

# -Sıralıdır
# -Değiştirilebilir
# -Kapsayıcıdır



x=["Fatih","Bilge","Dedem","Emo"]
type(x)
not_string=[]

for i in x:
    not_string.append(i)
print(not_string)   

#########################################
#- Liste Metodları



# -append:Diziye eklme işlemi yapar
x=["Fatih","Bilge","Dedem","Emo"]
type(x)
not_string=[]

for i in x:
    not_string.append(i)
print(not_string) 
######################################################
#-extend:Birden fazla eleman eklemek için kullanılır
x=["Fatih","Bilge","Dedem","Emo"]
y=["Ahmet","Mehmet"]
x.extend(y)
print(x)

######################################################
#-insert:Belirtilen indekse eleman eklemek için kullanılır
x=["Fatih","Bilge","Dedem","Emo"]
x.insert(2,"Ahmet")
print(x)

######################################################
#-remove:Belirtilen elemanı silmek için kullanılır
x=["Fatih","Bilge","Dedem","Emo"]
x.remove("Bilge")
print(x)

######################################################
#-pop:Belirtilen indeksteki elemanı silmek için kullanılır
x=["Fatih","Bilge","Dedem","Emo"]
x.pop(1)
print(x)
#-index:Belirtilen elemanın indeksini bulmak için kullanılır

######################################################
x=["Fatih","Bilge","Dedem","Emo"]
print(x.index("Bilge"))

######################################################
#-count:Belirtilen elemanın kaç kez tekrar ettiğini bulmak için kullanılır
x=["Fatih","Bilge","Dedem","Emo","Bilge"]
print(x.count("Bilge"))

######################################################
#-sort:Diziyi sıralamak için kullanılır
x=["Fatih","Bilge","Dedem","Emo"]
x.sort()
print(x)

######################################################
#-reverse:Diziyi tersine çevirmek için kullanılır
x=["Fatih","Bilge","Dedem","Emo"]
x.reverse()
print(x)

######################################################
#-clear:Diziyi temizlemek için kullanılır
x=["Fatih","Bilge","Dedem","Emo"]
x.clear()
print(x)

######################################################
# -Copy:Diziyi kopyalamk için kullanılır
x=["Fatih","Bilge","Dedem","Emo"]
y=x.copy()
print(y)
