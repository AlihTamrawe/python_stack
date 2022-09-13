class BankAccount:
  def __init__(self, int_rate, balance) :
    self.int_rate = int_rate
    self.balance = balance

  def deposit(self, amount):
    self.balance+=amount
    return self

  def withdraw(self, amount):
    if self.balance -amount > 0 :
      self.balance-=amount
    else:
      print('insuffecient funds')
    return self


  def display_account_info(self):
    print(f"your balance :{self.balance}")
    return self

  def yield_interest(self):
    if self.balance >0 :
      self.balance = self.balance*self.int_rate + self.balance
      return self



class User:
  def __init__(self, name, email, age):
    self.name=name
    self.email=email
    self.age=age
    self.account= BankAccount(int_rate=0.12,balance=2500)
    
  def withdraw(self , amount ):
        self.account.withdraw(amount)
        return self
    
    
  def display_user_balance(self):
    self.account.display_account_info()
  def depositt(self, amount):
    self.account.deposit(amount)
    return self


saeed = User('saeed', 'saeed@email.com', 25)
ahmad = User('ahmad', 'ahmad@email.com', 23)
ali = User('ali', 'ali@email.com', 29)

saeed.depositt(10000).depositt(29909).depositt(9000).withdraw(20000).display_user_balance()

ahmad.depositt(299009).depositt(9000).withdraw(20000).display_user_balance()



ali.depositt(1000000).withdraw(20000).withdraw(20000).withdraw(20000)