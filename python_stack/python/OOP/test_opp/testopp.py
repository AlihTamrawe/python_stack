class user:
    def __init__(self,name,email,age):
        self.name=name
        self.age=age
        self.email=email
        self.account_balance=0
        self.greeting()
    def deposit(self,dep):
        self.account_balance+=dep
    def get_balance(self):
        return self.account_balance
    def greeting(self):
        self.get_balance()
        print("hi",self.name)


ali = user("ali","a@gmail",25)
ali.deposit(100)



