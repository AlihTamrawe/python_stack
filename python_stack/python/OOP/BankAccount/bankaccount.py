class BankAccount:
  def __init__(self, int_rate, balance) :
    self.int_rate = int_rate
    self.balance = balance

  def deposit(self, amount):
    self.balance+=amount
    return self

  def withdraw(self, amount):
    if self.balance-amount > 0 :
      self.balance-=amount
      return self
    else :
      print("insuff ...")

  def display_account_info(self):
    print(f"your balance :{self.balance}")
    return self

  def yield_interest(self):
    if self.balance >0 :
      self.balance = self.balance*self.int_rate + self.balance
      return self

ali = BankAccount(0.25, 1000)
ali.deposit(1000).deposit(1000).deposit(800).withdraw(200).yield_interest().display_account_info()


ahmad = BankAccount(0.157, 7000)
ahmad.deposit(1000).deposit(2000).withdraw(800).withdraw(2000).yield_interest().display_account_info()




