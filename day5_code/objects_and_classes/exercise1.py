class Calculator:
    def __init__(self):
        self.operations_history = []

    def add(self, num1, num2):
        print("adding")
        print(self)
        vysledek = num1 + num2
        self.operations_history.append(
            f"added {num1} to {num2} got {vysledek}"
        )
        return vysledek

    def multiply(self, num1, num2):
        vysledek = num1 * num2
        self.operations_history.append(
            f"multiplied {num1} by {num2} got {vysledek}"
        )
        return vysledek

    def print_operations(self):
        for operation in self.operations_history:
            print(f"Operation: {operation}")

calc = Calculator()

cislo1 = 5
cislo2 = 50

soucet = calc.add(cislo1, cislo2)

soucet2 = calc.add(10, 60)

soucet3 = calc.add(100, 600)
