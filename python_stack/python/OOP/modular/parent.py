local_val = "magical unicorns"
def square(x):
    return x * x
class product:
    def __init__(self,number,name,price):
        self.name=name
        self.number=number
        self.price=price
        print("created product ")
        self.show_price()
    def update_price(self, percent_change, is_increased):
        pass
    def show_price(self):
        print(f"the price of{self}:{self.price}$")



class User:
    def __init__(self, name):
        self.name = name
    def say_hello(self):
        return "hello"
print(square(5))
user = User("Anna")
print(user.name)
print(user.say_hello())
print(__name__)
if __name__ == "__main__":
    print("the file is being executed directly")
else:
    print("The file is being executed because it is imported by another file. The file is called: ", __name__)

