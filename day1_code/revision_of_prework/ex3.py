import random

random_number = random.randint(0, 5)

print(f"random_number: {random_number}")

for i in range(random_number):
    for j in range(i + 1):
        print("*", end="")
    print()



# Lukas

# from random import randint

# size = randint(3, 9)

# print(f'size: {size}')

# for i in range(size):
#     j = i + 1
#     asterixes = []
#     for n in range(j):
#         asterixes.append('*')
#     print(''.join(asterixes))