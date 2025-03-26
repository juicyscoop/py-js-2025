from math import pi

class Circle:
    def __init__(self, r):
        self.r = r
    
    def area(self):
        return pi * self.r ** 2
    
    @staticmethod
    def static_area(r):
        return pi * r ** 2
    
    @classmethod
    def from_area(cls, area):
        r = (area/pi)**(1/2)
        return cls(r)
        # return Circle(r)

    @property
    def get_area(self):
        return pi * self.r ** 2
    
    @area.setter
    def set_area(self, new_area):
        self.r = (new_area/pi)**(1/2)

instance_kruhu = Circle(5)
print("Plocha kruhu: ", instance_kruhu.area())

# Vypocet plochy bez instance
print("Plocha kruhu o polomeru 10: ", Circle.static_area(10))

# Vytvoreni instance kruhu z jeho plochy
kruh_z_plochy = Circle.from_area(64)
