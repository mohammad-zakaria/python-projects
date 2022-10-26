""" Managers Bank Accounts """


class Account:

    accountID = 1

    def __init__(self, name, age, nid_no, balance):
        self.name = name
        self.age = age
        self.nid_no = nid_no
        self.balance = balance

         #update account id
        self.account_id = Account.accountID
        Account.accountID += 1

    def deposit(self, amount):
        self.balance += amount
    
    def withdraw(self, amount):
        if(self.balance >= amount):
            self.balance -= amount
        else:
            print("Insufficient Balance")



acc_1 = Account("John", 25, "123456789", 1000)
acc_2 = Account("Jane", 30, "987654321", 2000)

# print(acc_1.name)
# print(acc_1.account_id)
# print(acc_2.account_id)

acc_1.deposit(1000)
print(acc_1.balance)

acc_1.withdraw(2500)
print(acc_1.balance)