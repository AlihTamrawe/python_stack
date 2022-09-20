import parent
from modular.parent import product
from modular.parent import User

par =User()

if __name__ == "__main__":
    product = product(123,'ali',55)
    print(product)
    print(product.update_price(0.18))