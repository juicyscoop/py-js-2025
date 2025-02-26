
def divide(a, b):
    try:
        a, b = int(a), int(b)
        return a / b
    except ValueError:
        print(f"Not a number! {a, b}")
        return None
    except ZeroDivisionError:
        print(f"Nelze delit nulou!")
        return None

print(divide(10,2))
print(divide(10,0))