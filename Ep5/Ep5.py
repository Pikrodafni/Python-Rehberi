# < < ** File Operations ** > >

fp = open("C:\\Users\\HP\\Desktop\\Python.txt","r+")  # r read için w write için a append için

# content = fp.read() # read içine sayı yazıp kaç karakter okunucak seçebiliyoruz.
# read string olarak okur

# content = fp.readlines()
# readlines list biçiminde sonuç verir

# content = fp.readline()
# readline sadece ilk satırı okur
# print(content)

# for x in fp: # bu şekilde de okunabilir
#     print(x)

fp.write("hi hello")
print(fp.tell())
fp.seek(0,0)
content = fp.read()
print(fp.tell())
print(content)
print(fp.tell())    
# tell hangi karakterde olduğunu söyler yerini
# seek yer değiştirme yerini değiştirir bulundugun yeri