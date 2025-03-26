

class Circle:
   # radius (polomer)
    #area (plochu)
    pass
    def set_radius(self, new_radius):
        self.radius = new_radius
        self.area = pi * new_radius**2

    def set_area(self, new_area):
        self.area = new_area
        self.radius = (new_area/pi)**(1/2)

c = Cirle(radius=3)
c.set_radius(6)