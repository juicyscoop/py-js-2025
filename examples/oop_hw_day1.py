
#
    # name (str)
    # amount of protein in 100g of product (float or int)
    # amount of carbohydrates in 100g of product (float or int)
    # amount of fats in 100g of product (float or int)

class Ingredient:
    def __init__(self, name: str, protein_amount: float, carbohydrates_amount: float, fats_amount: float):
        self.name = name
        self.protein_amount = protein_amount
        self.carbohydrates_amount = carbohydrates_amount
        self.fats_amount = fats_amount

class Meal:
    def __init__(self, name: str):
        self.name = name
        self.list_of_ingredients = []

    def add_ingredients(self, list_of_ingredients: list[tuple[int, Ingredient]]):
        # na vstupu
        
        # [(100, vajca), (200, cukr)]

        self.list_of_ingredients.append(list_of_ingredients)


m = Meal("lunch")
m.add_ingredients(
    [
        (100, Ingredient("egg", 10, 20, 30)),
        (200, Ingredient("sugar", 10, 20, 30)),
    ]
)
