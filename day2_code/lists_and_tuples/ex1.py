
def create_list(a, b):
        seznam = []
        for i in range(4):
                seznam.extend([a, b])
        return seznam

def create_list_vojtech(a,b):
    result = [(a,b)*4]
    return result

def create_list_lukas(a, b):
        return [item for _ in range(4) for item in (a, b)]

print(create_list_vojtech("a","b"))
