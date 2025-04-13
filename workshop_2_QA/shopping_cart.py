from collections import defaultdict

class Product:
    _id_counter = 0

    def __init__(self, name: str, price: float):
        if not isinstance(name, str):
            raise ValueError("Product name must be string!")
        if not isinstance(price, (int, float)):
            raise ValueError("Product price must be int or float!")
        
        self.name = name
        self.price = price
        self.id = Product._id_counter
        Product._id_counter += 1


class ShoppingCart:
    def __init__(self):
        self.products = {}
        self.quantities = defaultdict(int)

    def add_product(self, product: Product):
        self.products[product.id] = product
        # if product.id not in self.quantities:
        #     self.quantities[product.id] = 0
        self.quantities[product.id] += 1

    def remove_product(self, product: Product):
        if product.id in self.products:
            del self.products[product.id]
            del self.quantities[product.id]

    def change_product_quantity(self, product: Product, new_quantity: int):
        if product.id not in self.products:
            return

        if new_quantity == 0:
            self.remove_product(product)
        elif new_quantity < 0:
            raise ValueError("Quantity cannot be negative!")
        else:
            self.quantities[product.id] = new_quantity
    
    def get_receipt(self):
        s = ""
        
        for product_id, product in self.products.items():
            product_quantity = self.quantities[product_id]
            product_string = f"{product.name} - quantity: {product_quantity}, price: {product.price} EUR, total: {product_quantity*product.price} EUR \n"
            s += product_string

        return s
    

if __name__=="__main__":
    bread = Product('Bread', 2.70)
    ham = Product('Ham', 8.40)
    cheese = Product('Cheese', 4.40)
    chive = Product('Chives', 1.50)
    pepper = Product('Pepper', 2.35)

    cart = ShoppingCart()

    print(cart.products)
    print(cart.quantities)

    cart.add_product(bread)
    cart.add_product(bread)
    cart.add_product(bread)
    cart.add_product(pepper)
    cart.add_product(chive)

    print(cart.products)
    print(cart.quantities)
    
    print(cart.get_receipt())