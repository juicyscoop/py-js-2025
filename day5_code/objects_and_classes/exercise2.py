class Shape:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color

    def describe(self):
        return self.x, self.y, self.color

    def distance(self, other):
        # Tato metoda meri vzdalenost mezi
        # stredem tohoto objektu a "other" objektu
        return (
                abs(self.x - other.x)**2 + abs(self.y - other.y)**2
        )**(1/2)

    def __str__(self):
        return f"Figure of the {self.color} color with center at point ({self.x}, {self.y})."

shape1 = Shape(1, 5, "black")
popis_shape1 = str(shape1)
print("popis shape 1: ", popis_shape1)

shape2 = Shape(2, 10, "white")
popis_shape2 = str(shape2)
print("popis shape 2: ", popis_shape2)

vzdalenost_mezi_stredy_shape1_shape2 = shape1.distance(shape2)
print(vzdalenost_mezi_stredy_shape1_shape2)
