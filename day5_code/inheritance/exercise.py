class Cart:
    def __init__(self):
        self.products = []

    def add(self, price, name):
        if not isinstance(price, (int, float)):
            raise TypeError("Price must be int or float!")
        if not isinstance(name, str):
            raise TypeError("Product name must be string!")
        self.products.append((name, price))

    def summary(self):
        return self.products

class Discount20PercentCart(Cart):
    def summary(self):
        #return [(name, price*0.8) for name, price in self.products]
        products_with_20_perc_sale = []
        for i in self.products:
            product_name = i[0]
            product_price = i[1]
            sale_price = product_price * 0.8
            products_with_20_perc_sale.append(
                (product_name, sale_price)
            )
        return products_with_20_perc_sale

class Above3ProductsCheapestFreeCart(Cart):
    def summary(self):
        if len(self.products) > 3:
            # Budeme zlevnovat nejlevnejsi produkt
            cheapest_product_price = min([i[1] for i in self.products])

            products_with_cheapest_for_free = []

            for i in self.products:
                product_name = i[0]
                product_price = i[1]

                if product_price == cheapest_product_price:
                    product_price = 0

                products_with_cheapest_for_free.append(
                    (product_name, product_price)
                )
                return products_with_cheapest_for_free

        else:
            return self.products

