from math import pi

class Circle:
    def __init__(self, r):
        self.r = r  # in meters

    def area(self):
        return pi * self.r ** 2

    @classmethod
    def from_area(cls, area):
        r = (area/pi)**(1/2)
        return cls(r)


c1 = Circle(5)
print(c1)
c2 = Circle.from_area(64)
print(c2)