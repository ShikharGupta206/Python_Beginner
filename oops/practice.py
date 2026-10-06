# Average

# class Student:
#     def __init__(self,name,marks):
#         self.name=name
#         self.marks=marks
#     def get_avg(self):
#         sum=0
#         for value in self.marks:
#             sum+=value
#         print("hi",self.name,"your avg score is",sum/3)

# s1=Student("karna",[97,98,92])
# s1.get_avg()

# Account class

class Account:
    def __init__(self,balance,account_no):
        self.balance=balance
        self.account_no=account_no

    def debit(self,amount):
        self.balance-=amount
        print("Your account debit is",amount)
        print("total balance=",self.balance)

    def credit(self,amount):
        self.balance+=amount
        print("Rs.",amount,"was credited in your account")
        print("total balance=",self.balance)
    def get_balance(self):
        print("Your balance is",self.balance)


acc1=Account(10000,22922)
acc1.debit(10000)
acc1.credit(29292929)
acc1.debit(23456)

