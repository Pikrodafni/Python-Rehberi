print("Merhaba evlat!!!")

f_num = 10
s_num = 20.2
str = "Merhaba"
print(f_num, str, s_num)
# type of variable show with type function
print(type(f_num), type(s_num), type(str))
# memory Allocation show with id
print(id(f_num), id(s_num), id(str))
a = 10
num1 = 100
print(type(num1))
print(id(num1))

s = " 'Python' Another string"
print(s, id(s))
# string veya int farketmez liste oluşturma [1,2,3,4,"adana","mardin]
samp_list = ['adana', 'bursa', 'mardin']
l2 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
print(l2)
print(samp_list)
# normal listeye eklemeler yapılınabilir
l2.append(10)
print(l2)
# Non-Change değişken tuple içine ekleme çıkarma yapılamaz
rakam = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
print(rakam)

# Dict veritabanındaki gibi bir key var onun içinde listeler var örnek "isim": "orkun" gibi isim: içine 1 den fazla
# eklenemez

dict = {"isim": "orkun", "e-mail": "orkunalkan98@gmail.com"}
print(dict)

# dir kullanılabilicek komutları gösterir
print(dir(dict))
# uzunluk belirtmek len
print(len(dict))
# in parametresi değişken içinde olup olmadığını gösterir
print("isim" in dict)  # içinde mi diye kontrol in
# silme işlemi del
del (dict["isim"])
print(dict)
# clear tüm key'leri siler
dict.clear()
print(dict)
# ekleme yapma
dict["bir"] = "uno"
# kopyalama
D2 = dict.copy()
print(D2)
# anlamadım -------
s = {1, 2, 3, 4, 5, 6, 7, 8, 9,"klei"}
print(s)
# --------
# bildiğimiz bool true false değerleri koyulan
bool = True
print(bool)
bool = False
print(bool)
# complex real ve irreal kökenli sayı konuyor tam olarak ne işe yara bilmiyorum
complex: 3j + 4
# ------------ Operators in Python ----------------
# Arithmetic Operators +, -, /, *, %, //, **
num1 = 10
num2 = 20
print(num1 / num2, num2 / num1)
print(100 / 3)  # / bölme işareti float sonuç verir
print(100 // 3)  # // işareti bölmenin sonucunu integer çevirir
print(10 * 3)  # * 10 ile 3 ü çarpar
print(10 ** 3)  # 10 üssü 3 sonucunu verir **
print(10 % 3)  # 10 sayısının 3 modunu alır ve sonucu verir
# --------------------------------------------------
# ------------ Comparison Operators  <,>,<=,>=,==,!=

num1 = 100
num2 = 200

print(num1 == num2) # --------- eşit mi diye bakar----------
print(num1 != num2) # --------- eşit değil mi diye bakar ----------

# ----------------------------------------------------
# ------------ Identify Operators is, is not

print("is denemesi : ", num1 is num2)

l = [1, 2, 3]
l2 = [1, 2, 3]
# aşağıda liste karşılaştırmasında is == ile aynı sonucu vermez çünkü python aynı sayı olduğunda memory allocation aynı
# fakat liste olduğunda memory yerleri aynı değil is ile bellekteki yerini kontrol ediyoruz o yüzden false veriyor
print(l == l2)
print(l is l2)
# -----------------------------------------------------
# ------------- Assignment Operators =,+=,-=,*=,/=
num1 = 100
num1 += 10
print(num1)
# ------------------------------------------------------
# -------------- Bitwise Operators &,|,^,>>,<<

num_bin1 = 1
num_bin2 = 2
print(bin(num_bin1), bin(num_bin2))
print(num_bin1 & num_bin2)
print(num_bin1 | num_bin2)
# --------------------------------------------------------
# --------------- Logical Operators and, or, not

# --------------------------------------------------------
# ---------------- Membership Operators in, not in

l = [1,2,3,4,5,6,7,8,9,10]
print(10 in l)
print(11 not in l)
l.append(11)
print(11 in l)
# --------------------------------------------------------
# ----------------- Conditional Statements if, elif ,else
num1 = 100
num2 = 200

if num1 > num2 :
    print("num1 greater than num2") # num1 dahga büyük ise
elif num1 == num2 :
    print("num1 equal with num2") # num1 ve num2 eşit ise
else:
    print("num1 is not greater than num2") # num1 num2'den büyük değil ise

# -----------------------------------------------------------
# ------------------ Loops for in , while
# Iterable Datatypes
# str, tuple, list, dict, set

# for [variable_name] in [Iterable_datatype]:
# statements...

# range(5) 0,1,2,3,4,5
# range(10,1000) 10,11,12,13,14,15...1000
# range(10,1000,5) 10,15,20,25,30,35,40,45,50....1000

k1 = [10,20,30,40,50]
sum = 0
for value in k1:  # value sırasıyla k1 içindeki sayıları alıyor ve sona doğru gidiyor
    sum += value
    print(sum)

for value in range(5):
    print(value)

l = [10,20,30,40,50,60,70]
key = 41

for value in l:
    if value == key:
        print("Element found")
        break
    else:
        continue
else:
    print("Element not found")

for index,value in enumerate(l): # index içine l listesindeki değerler enumerate yani sırası yazdırılıyor.
    print(index,value)

count = 1
sum = 0

while count <= 20:
    sum = sum + count
    count += 1

print("sum:",sum)