# cust id
# name
# balance
#
# deposite
# withdraw


class Account:
    count = 0
    @classmethod
    def incr_count(cls):
        cls.count+=1

    @classmethod
    def get_count(cls):
        return cls.count

    @ staticmethod
    def print_Val():
        print("Static method in account class")
    def __init__(self,cust_id,name,initial_bal=0):
        self.__id = cust_id
        # eğer ki class içindeki değişkenlerin başına self.__id olarak yazarsak değiştirilmesi yasaklanır
        # çağırmak için özelliklerin tek tek def get_id tarzında fonksiyonlarını yazmalıyız
        self.__name = name
        self.__balance = initial_bal
        Account.incr_count()
    def get_balance(self):
        return self.__balance
    def deposite(self,ammount):
        self.__balance = self.__balance + ammount
        return self.__balance

    def withdraw(self,ammount):
        if ammount > self.__balance:
            return "Insufficient balance"
        else:
            self.__balance -= ammount
            return self.__balance

customer1 = Account("101","ABC")
# Account(customer1,"101","ABC")
print(customer1)
# print(customer1.id,customer1.name,customer1.balance)
print(customer1.get_balance())
print(customer1.deposite(100))
print(customer1.withdraw(25))
print(customer1.withdraw(76))
print(Account.count)
# print(customer1.get_balance())


customer2 = Account("102","ABCD")
print(customer2)

customer2 = Account("103","ABCDE")
print(customer2)

print(Account.get_count())
Account.print_Val()


class Saving_Account(Account):
    def __init__(self,id,name,initial_bal=0):
        super().__init__(id,name,initial_bal)
        self.limit = 50000
    def withdraw(self,ammount):
        if ammount < self.limit:
            new_bal = super().withdraw(ammount)
            self.limit -= ammount
            return new_bal
        else:
            print("Daily limit reached")


cust1 = Saving_Account(12,"asa")
print(cust1.__dict__)
print(cust1.deposite(80000))
print(cust1.withdraw(10000))
print(cust1.withdraw(45000))