for i in range(1500,2700):
    if i%5==0 and i%7==0:
        print("divisible to 7 and 5 :",i)

l = [1,2,3,4,5,6,7,8,9,10,11]
countEven = 0
countOddd = 0
for i in l:
    if i%2 == 0:
        print("even number :",i)
        countEven += 1
    else:
        print("odd numbers :",i)
        countOddd += 1

print("Number of even numbers :",countEven,"\nNumber of odd numbers :",countOddd)
