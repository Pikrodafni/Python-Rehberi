# string
s = "Python sample string"
print(type(s),id(s))
# -------- indexing ------------
for i in range(0,10):
    print(s[i])
# ------------ slicing ------------
print(s[0:5],"//",s[7:])
# -----------------------------------------------------------------------------------------------------------
# ---------------------------------------- PYTHON GENEL KULLANIM --------------------------------------------
num1 = 100
num2 = 200
print("value of num1 is {1} num2 is {0}".format(num1,num2))

s1 = "PYTHon The Field"
s1=s1.capitalize() # düzenleme baş harf büyük diğerleri küçük
print(s1)
print(s1.upper()) # tüm karakterler büyük
print(s1.lower()) # tüm karakterler küçük
print(s1.title()) # tüm kelimelerin ilk harfi büyük
print(s1.isupper()) # is upper yani hepsi büyük mü is lower (s1.islower) hepsi küçük mü diye bakar true false döner
languages = "Java,Python,C,C#,HTML,CSS"
print(languages)
seperatelang = languages.split(",") # liste haline dönüştürür arada , olanları ayırdı
print(seperatelang[1])
print(seperatelang)
joinlang = (" ").join(seperatelang) #  virgül olanları ayırıp liste yapılmıştı şimdi arada boşlukla stringe çevrildi
print(joinlang)

a = "abcd"
b = "1234"
s = "Python Sample string abcd"

table = str.maketrans(a,b) # a dan b ye çevirme yapması için table'ı translate aracı belirliyoruz.
result = s.translate(table) # s içinde bulunan table maketransı yani abcd yi 1234 e çeviriyor.

print(result)

s = "HTML,CSS,PYTHON,PYTHON,PYTHON"
print("PYTHON" in s) # python s stringinin içinde mi diye bakar
print(s.index("PYTHON")) # python s içindeki indexi gösterir find ile farkı ne yazmamışım.
print(s.find("PYTHON")) # ilk python indexini bulur
print(s.rfind("PYTHON")) # sondaki python indexini bulur

s = "******Sample String is this**********"
s = s.strip("*") # başı temizler
s = s.rstrip("*") # sonu temizler
print(s)
s = "hihello"
s1 = s.center(40,"-") # iki yana da ekler
s1 = s.ljust(20,"*") # sadece sola ekler rjust da sadece sağına ekler
print(s1)
gs = "html,css,python,java"
s2 = gs.replace("html","HTML5") # Yerine ekleme replace
print(s2)
# -----------------------------------------------------------------------------------------------------
# ----------------------------------------- LİSTE KULLANIMI -------------------------------------------
l = [10,20,30,40,50,60,70,80,90,100]
print(l,type(l))
for value in l [::2]: # atlamalı olarak bak 2 şer atlama 3 yaparsan 3 lü atlama
    print(value)
# --------- append list --------------- LİSTEYE EKLEME --------------------------------------
print(l)
l.append(110) # tek sayı ekleme
l.extend([120,130,140,150,160,170,180,190,280]) # toplu değer ekleme
l.extend("Python")
print(l)
l.insert(1,1000) # index belirtip araya ekleme 1 indexine 1000 sayısını koyar 1 de olandan itibaren değişkenleri
# sağa kaydırır 1 indexindekini 2 ye mesela 2 -> 3   3 -> 4
print(l)

l2 = l.copy() # l LİSTESİNDEKİ DEĞİŞİKLİK l2 YE ETKİ ETMESİN İSTİYORSAK l.copy() KOMUTUNU KULLANMALIYIZ
print(l2)

# index içini değişme
lis = [10,20,30,40,50]
lis[2] = 300
r = lis.pop(1) # son indexi çıkarır ve aktarır pop( ) içine index belirtirsek orayı çıkarır
print(lis,r)
lis.remove(10) # direk yazılan değeri içinden çıkarma aynı değerden 2 tane varsa küçük olan indexden çıkarır
print(lis)
lis.clear() # tamamını temizler
print(lis)
del lis # tamamen değişkeni kaldırır
lis2 = [20,10,60,40,30]
lis2.sort() # küçükten büyüğe sıralar
print(lis2)
lis2.reverse() # ters çeviriyor
print(lis2)
l3 = sorted(lis2) # içine yazılan listenin sıralanmış halini kopyalamaya yarar
print(l3)
l.count(10) # içinde kaç tane 10 var ona bakar
print(l3+lis2) # art arda birbirine ekleyerek yazar
# --------------------------------------------------------------------------------------------
# -------------------------------------- TUPLE KULLANIMI--------------------------------------
# tuple listten farkı ekleme çıkarma silme yapılamaz
# count ve index fonksiyonları çalışır

t = (10,20,20,20,20,30,40)
print(t[:3])
print(t.count(20))

for index,value in enumerate(t):
    print(index,value)

t2 = [1,2,3,4,5,6,7,8,9]
print(t2)
t2 = tuple(t2)
print(t2)
t2 = list(t2)
print(t2)
# --------------------------------------------------------------------------------------------------------------
# --------------------------------------- DİCTİONARY TYPE KULLANIMI --------------------------------------------
# allow to only int, float, string and tuples
d = {"emp_id":98,"name":"orkun","age":20,"surname":"alkan","birth_date":2000}
print(d)
d["contact_no"] = 123654
print(d)
print(d["emp_id"])
print(d.get("emp_id"))
print(d.get("country","Key does not exist"))
print(d.setdefault("country","Turkey"))
print(d)
for x in d:
    print(x,"-->",d[x])
print(d.keys())
print(d.values())
print(d.items())

# dictionary oluşturma örnek olarak 2 listeyi birleştirme

l1 = [1,2,3,4,5]
l2 = [1,4,9,16,25]

dict2 = dict(zip(l1,l2))
print(dict2)
dict3 = dict.fromkeys(l1)
print(dict3)
dict2.update(d)
print(dict2)
# dict2.pop(2) 2 key adını dışarı atar örnek r = dict2.pop(2)
# popitem ise key 2 yi ve karşılığını atar 2: 4 r' nin içine gider r = dict2.popitem() bişey seçmezsek sondaki key gider
# dict2.clear dict2 içini temizler
# del dict2 değişkeni yok eder

# ---------------------------------------------------------------------------------
# ------------------------------ SET DATA TYPE KULLANIMI --------------------------
# set could be int, float, string and tuple
s = {1,2,3,4,5,6,7,8,9,1,2,3,4,5} # Duplicate yani tekrar eden sayıları göstermez
print(s,type(s))
s.add(11)
print(s)
print("-------------------")
s1 = {1,2,3,4,5,6,7}
s2 = {5,6,7,8,9,10}
s3 = s1.union(s2) # s1 ve s2 de olanları birleştiriyor s1 birleşim s2 küme gibi
s4 = s1.intersection(s2) # kesişimleri yazdırıyor s1 kesişim s2
s5 = s1.difference(s2) # ayrık olanları yazıyor s1/s2
s6 = s1.symmetric_difference(s2) # kesişim harici iki tarafında elemanlarını yazdırır
print(s3)
print(s4)
print(s5)
print(s6)
print(s1.issubset(s2)) # s1 kümesi s2 kümesinin alt kümesi mi değil mi diye true false veriyor
print(s1.issuperset(s2)) # s1 kümesi s2 kümesinin üst kümesi mi diye bakıyor true false veriyor
# -------------------------------------------------------
# ------------- LİSTEYİ SET YAPMA ------------
listele = [1,2,3,4,5,6,7,8,9]
listele = set(listele)
print(listele)
# clear, remove, pop gibi benzer kodlar burda da var ayrıca discard var aynı remove gibi seçilen elemanı kaldırıyor fakat
# tek farkı eleman set içinde bulunmasa bile hata vermiyor

# -------------------------------------------------------------------------------
# ----------------------- MATEMATİK FONKSİYONLARI VE RASTGELE SAYI MODÜLLERİ ---------------------------
l = [100,200,300,400,500]
print(sum(l)) # sum içine listeyi yazınca direk içindeki tüm elemanları topluyor izi :d
print(max(l)) # l listesindeki en büyük elemanı max ile buluruz
print(min(l)) # ""  en küçük elemanı min ile buluruz
num = 25.555
print(round(num)) # en yakın tam sayıya yuvarlama
print(round(num,2)) # yuvarlamadan sonunda kaç basamak gözüksün ayarı ne işe yarar ki (!)
print(dir(__builtins__)) # tüm kodları veriyor galiba sonlara doğru sağa doğru tanıdık kodlar var başta ..error vs var
# help(__builtins__) fonksiyon modüllerinin açıklamaları var uzun diye yorum satırına aldım

# -------------------------------------------------------
# ----------------- MATH KÜTÜPHANESİ --------------------
import math

l = [0.1] * 10
print(l)
print(sum(l)) # dümdüz topluyor
print(math.fsum(l)) # toplam sonucu yuvarlıyor
nums1 = 15.5559
print(math.floor(nums1)) # floor (anlamı zemin)sayının küsürata bakmaksızın aşağı yuvarlıyor
print(math.ceil(nums1)) # ceil de anlamı tavan zaten yukarı yuvarlıyor
print(math.sqrt(25)) # içine yazılan sayının kökünü alıyor
print(math.factorial(5)) # içine yazılanın faktöriyelini alıyor
print(math.modf(nums1)) # içine yazılan sayıyı tam sayı kısmı ve kesir kısmını ayırıyor
d , i = math.modf(nums1) # decimal kısmı ve integer kısmı ayrı ayrı atıyor
print(d,i)
print(math.pow(10,2)) # 10 üssü 2 yi alıyor
print(math.log(10,2)) # 10'un 2 tabanında logaritmasını alıyor
print(math.log10(2)) # 10 tabanında log2
print(math.sin(math.radians(90))) # sinüs vs vs math.radians ile yazınca açı girmiş oluyoruz sadece sayı girersek farklı

# help(math)
# print(dir(math)) yardım için bunlara başvurun :D

# ----------------------------------------------------------------
# ------------------- RANDOM NUMBER ------------------------------
import random

print(random.random()) # her seferinde farklı bir random veriyor
l = [1,2,3,4,5,6,7,8,9]
print(random.choice(l)) # l listesi içinden random sayı seçiyor
print(random.randint(1,3)) # 10 ve 100 arasında random sayı
print(random.randrange(1,3)) # randintten tek farkı sondaki sınır sayısını sonuç vermiyor 3 sınır dahil değil
print(random.uniform(10,20)) # float değerleri random veriyor