import random

def d6(num):
    s = 0
    for _ in range(num):
        hodnota_hodu = random.randint(1,6)
        print(f"hodnota_hodu: {hodnota_hodu}")
        s += hodnota_hodu
    return s

print(d6(4))
