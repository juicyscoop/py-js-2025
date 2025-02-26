

def safe_get(l, number):
    try:
        return l[number]
    except IndexError:
        return None

seznam = [1,2,3,4]
print(safe_get(seznam, 0))
print(safe_get(seznam, 5))