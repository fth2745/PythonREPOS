#Örnek-1
"""numbers = [3,5,45,97,32,22,10,19,39,43]
result = []
for number in numbers:
  if number % 2 == 0:
    result.append(number)
print(result)
#------------------------------------------------#
result=[number for number in numbers if number % 2 == 0]
print(result)"""
########################################################
#Örnek-2
"""dizi=list(range(1,1000))
yedi=[num for num in dizi if num%7==0]
print(yedi)"""
########################################################
#Örnek-3
"""dizi2 = list(range(1, 1000))

# dizi2'yi string elemanları olan bir listeye çevir
dizi2_str_list = list(map(str, dizi2))

# '3' içeren elemanları seç
dizi = [num for num in dizi2_str_list if '3' in num]

print(dizi)"""
#######################################################
#Örnek-4
"""dizi="Bilge beni sevmek yerine bana tapıyo"
dizi2=[word for word in dizi if word==" "]
print(len(dizi2))"""
#######################################################
#Örnek-5
"""unluler=["a","e","ı","i","o","ö","u","ü"," "]
dizi="Sarı Yaklar bağırmayı ve esnemeyi sever ve dün yuky yam yerken yodlardı"
dizi_unsuz=[word for word in dizi if not word in unluler]
print(dizi_unsuz)"""
#######################################################
#Örnek-6
"""Dizi=['hi', 4, 8.99, 'apple', ('t,b','n')]
dizi=[(f"{a} .  indeks değeri --> {b}") for a,b in enumerate(Dizi)]
print(dizi)

"""
#######################################################
#Örnek-7
"""list_a=1,2,3,4,5
list_b=1,2,8,9,10

a=[x for x in list_a if x in list_b]
print(a)
"""
#######################################################
#Örnek-8
"""a="1984'te 1000'den fazla kişinin katıldığı 13 protesto örneği vardı"
words = a.split()
c=[b for b in words if not b.isalpha()]
print(c)"""
#######################################################
#Örnek-9
"""a=range(20)

b=[print(f"{c} çifttir") if c%2==0 else print(f"{c} tektir")  for c in a ]
"""
#######################################################
#Örnek-10
"""dizi = ["İstanbul", "Ankara", "İzmir", "Bursa", "Antalya","of","Fth"]
a=[b for b in dizi if len(b)<=4]
print(a)"""
#######################################################
#Örnek-11
"""divisible_numbers = [number for number in range(1, 1001) if any(number % divisor == 0 for divisor in range(2, 10))]
divisible_numbers=set(divisible_numbers)
x=set(range(1,1000))
y=x.difference(divisible_numbers)
print(y)"""
#######################################################




