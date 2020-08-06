# ----------------------------------- USER DEFİNED FUNCTİONS --------------------------------------

s = "Python,HTML,CSS"
print(s.index("HTML"))
s = "Python"
def value_reverse(value):
    reverse = value[::-1]
    print(reverse)
    return reverse
s = value_reverse(s)
print(s)
# --------------------------------------------------------------------------------------------
# -------------------------- PARAMETER PASSİNG TECHNİQUES ------------------------------------
# Positional Argument
def linear_search(l,key):
    for value in l:
        if key==value:
            return True
    else:
        return False

l = [100,200,300,400,500]
key = 400
result = linear_search(l,key)
print(result)
# --------------------------
# Default Argument
# --------------------------
print(ord('a'))
print(chr(97))
import random
def gen_password(length=8):
    l = ['@','#','$','&']
    upper = chr(random.randint(65,90))
    lower = chr(random.randint(97,122))
    special = random.choice(l)
    digits = random.randint(10000,99999)
    password = upper + lower + special + str(digits)
    l = random.sample(password,length)
    print(l)
    password = ("").join(l)
    return password
result = gen_password(5)
print(result)
# -------------------------
# Keyword Argument
# -------------------------
def validate(username,password):
    if username == "ABC" and password == "Abc@123":
        print("Valid password")
    else:
        print("İnvalid password")

validate("ABC","Abc@123")

# Kısa bilgi
print(100,200,sep=",",end=" ")
print("hi")

#------------------------------------------
# Varianble length positional args
#------------------------------------------
l = [100,200,300,400,500,600,700,800,900,1000]
l.append(150)

def add_value(*args): # sayı belirtmeksizin fonksiyon içine değer atabiliyoruz
    l = []
    for value in args:
        l.append(value)

    return l

result = add_value(100,200,300,400,500)
print(result)
result2 = add_value(100,200,300)
print(result2)

# -----------------------
# Variable length keyword args
# -----------------------
def get_details(**kwargs): # sayı belirtmeksizin fonksiyon içerisine değişken atabiliyoruz
    print(kwargs)
get_details(name = "ABC",email = "abc@gmail.com",contact = 7123456789,dob = "12-05-1890")

#---------------------------
#Recursive Functions ------------------------
#---------------------------

def factorial(num):
    if num == 1:
        return 1
    else:
        return num * factorial(num-1)

num1 = 5
result = factorial(num1)
print(result)

def binary_search(l,key):
    if len(l) == 0:
        return False
    else:
        mid = len(l) // 2
        if l[mid] == key:
            return True
        elif key < l[mid]:
            return binary_search(l[:mid],key)
        else:
            return binary_search(l[mid+1:],key)
if __name__ == '__main__':  # yan modüle import ettiğimiz bu modüldeki çıktıların orda çalışmasını engeller
    l = [100,200,300,400,500,600,700,800,900]
    key = 700
    result = binary_search(l,key)
    print(result)
    print(__name__)