
#@dataclass
#class Car:
#    name: str = "Citroen"
#    weight: int = 5

class Object:




class Car:
    def __init__(self, name):
        self.name = name
    def __lt__(self, other):
       return len(self.name) < len(other.name)
    def __repr__(self):
        return "Printing car instance"
    def car_is_smaller_than(self, car2):
        return len(self.name) < len(car2.name)



citroen_car = Car("Citroen")
bmw_car = Car("BMW")

print(citroen_car.name)
print(bmw_car)
print(citroen_car.car_is_smaller_than(bmw_car))
print(citroen_car > bmw_car)

#x = 2
#del x
#(x.__del__)