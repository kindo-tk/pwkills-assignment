class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

    def __repr__(self):
        return f"Product(name={self.name}, price={self.price}, stock={self.stock})"

def create_product(name, price, stock):
    return Product(name, price, stock)
