

class Car:
    def __init__(self, name):
        self.name = name

    def start(self):
        pass

class Citroen(Car):
    def start(self):
        super().start()
        # Citroen specific start code
        pass


citr = Citroen("c4")
citr.start()