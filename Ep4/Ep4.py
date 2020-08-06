# ------------------------------------ FUNCTİONAL PROGRAMMİNG ------------------------------------------
# List Comprehension
l = [100,200,300,400,500]
l2 = [value*value for value in l]
print(l2)


for value in l:
    l2.append(value*value)

print(l2)

# -----
l = [10,20,25,30,35,60,65,70,85]
l2 = [value for value in l if value%2 == 0]
print(l2)
# -----
l = ["abc","abcd","abcde","zzzzzz"]
l2 = [len(value) for value in l ]
print(l2)
# -----
l2 = [(value,value2)for value in range(1,5) for value2 in range(100,103)]
print(l2)
# -----
l = [[1,2,3],[4,5,6],[7,8,9]]
l2 = [(val2)for value in l for val2 in value]
print(l2)
# -----
l = [100,105,110,115,120]
l2 = ["Even" if value%2 == 0 else "Odd" for value in l]
print(l2)
# -----
d = {x:x**2 for x in range(1,11)}
print(d)
# -----
d = {chr(x):x for x in range(97,123)}
print(d)
# -----
d2 = {value:key for key,value in d.items()}
print(d2)
# ------------------------------------------------

# -------------------------------- MAP - FİLTER - LAMBDA --------------------------------------

def sqr(num1):
    return num1**2

l = [10,20,30,40,50]
result = list(map(sqr,l)) # map fonksiyonu içine yazılan sqr fonskiyonuna l içindekileri sırayla gönderir ve
# result içine atanır çıkan sonuçlar
print(result)
result = list(map(lambda num1:num1**2,l)) # lambda çok kısa fonksiyonları için kısa yazım şekli
print(result,"lambda ile olan")

for value in result:
    print(value)

def add(num1,num2):
    return num1+num2

l1 = [100,200,300,400]
l2 = [10,20,30,40]
res = list(map(add,l1,l2))
print(res)

def check_num(num1):
    if num1%2 == 0:
        return True
    else:
        return False

l = [100,115,120,125,130]

res = list(filter(check_num,l)) # filter olunca true olanları yazdırıyor sadece
print(res)
res = list(map(check_num,l)) # map olunca direk içinde ne çıkıyorsa true false döndürüyor
print(res)

def fibo():
    first_num = 0
    second_num = 1
    yield second_num
    while(True):
        next_val = first_num + second_num
        yield next_val
        first_num,second_num = second_num,next_val

g = fibo()

for value in range(10):
    print(next(g))

# <----------- ITERATORS AND ITERTOOLS ----------->

l = [100,200,300,400,500]
i = iter(l)
# print(i)

for value in i:
    print(value)

import itertools
# CHAİN
l1 = [10,20,30,40,50]
l2 = [100,200,300,400,500]
l3 = [1000,2000,3000,4000,5000]

i2 = itertools.chain(l1,l2,l3)
for value in i2:
    print(value)

# CYCLE

l = [10,20,30,40,50]
count = 0
for value in itertools.cycle(l):
    if count < 20:
        print(value)
    else:

        break
    count+=1

count = 0
for value in itertools.repeat(l):
    if count < 20:
        print(value)
    else:

        break
    count+=1
l = [1,2,3,4,5,6]

print(list(itertools.permutations(l,2))) # tüm olasılıkları veriyor önemli ! daha önce javada lazım oldu
# combinations hali de var