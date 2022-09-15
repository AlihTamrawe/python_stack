class Store:
    def __init__(self,products,name):
        self.name=name
        self.products=[]
        for i in range (len(products)):
            self.products.append(products[i])
        print("created Store ")
    def show_product(self):
        for i in range (len(self.products)):
            print(self.products[i]+" "+self.products[i])




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





koton = Store([product(1,"t_shirt",20),product(2,"toast",50),product(3,"toast",45)],"Koton",)
