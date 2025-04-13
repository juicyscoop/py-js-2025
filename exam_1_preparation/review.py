#from math import floor

# Jakub Slama
def dividers_js(number):
    for i in range(1, number + 1):
        if number % i == 0:
            yield i

def dividers(number: int):
    # Rozklad cisla > 0
    base = number
    if number < 1:
        raise ValueError("Number must be > 0")
    
    # Split number into
    #  prime numbers
    # Rozklad na prvocisla
    
    prvocisla = [1]
    delitel = 2
    # 1 bude vzdy vyprintena

    while number > 1:
        while number % delitel == 0:
            prvocisla.append(delitel)
            number = number // delitel
        delitel += 1

    if base not in prvocisla:
        prvocisla.append(base)

    return prvocisla

if __name__ == "__main__":
    for i in dividers(10):
        print(i)
