class User:
    def __init__(self, name, email):
        self.name = name 
        self.email =  email 
        self.account_balance = 100000

    def make_deposit(self, amount):
        self.account_balance += amount

    def make_withdrawal(self, amount):
        self.account_balance -= amount
    
    def display_user_balance(self):
        self.name, self.account_balance

prince = User("prince", "piwejuo@gmail.com")
collins = User("collins", "cebozue@gmail.com")
arinze = User("arinze", "aobiora@gmail.com")

collins.account_balance = 10000
arinze.account_balance = 7000

# prince.make_deposit(10000)
# prince.make_deposit(1000)
# prince.make_deposit(500)
# print(prince.account_balance)

# prince.make_withdrawal(11500)
# print(prince.account_balance)
# prince.display_user_balance

# print(prince.name, prince.account_balance)

# collins.make_deposit(500)
# collins.make_deposit(500)
# collins.make_withdrawal(1000)
# collins.make_withdrawal(500)
# collins.display_user_balance

# print(collins.name, collins.account_balance)

# arinze.make_deposit(4000)
# arinze.make_withdrawal(1000)
# arinze.make_withdrawal(500)
# arinze.make_withdrawal(2000)
# arinze.display_user_balance

# print(arinze.name, arinze.account_balance)