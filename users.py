class User:
    def __init__(self, name, email):
        self.name = name 
        self.email =  email 
        self.account_balance = 100000

    def make_deposit(self, amount):
        self.account_balance += amount
        return self

    def make_withdrawal(self, amount):
        self.account_balance -= amount
        return self
    
    def display_user_balance(self):
        self.name, self.account_balance
        return self

prince = User("prince", "piwejuo@gmail.com")
collins = User("collins", "cebozue@gmail.com")
arinze = User("arinze", "aobiora@gmail.com")

collins.account_balance = 10000
arinze.account_balance = 7000

prince.make_deposit(10000).make_deposit(1000).make_deposit(500)
print(prince.account_balance)

prince.make_withdrawal(11500).display_user_balance()
print(prince.account_balance)
print(prince.name, prince.account_balance)

collins.make_deposit(500).make_deposit(500).make_withdrawal(1000).make_withdrawal(500).display_user_balance()
print(collins.name, collins.account_balance)

arinze.make_deposit(4000).make_withdrawal(1000).make_withdrawal(500).make_withdrawal(2000).display_user_balance()
print(arinze.name, arinze.account_balance)