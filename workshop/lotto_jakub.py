from random import randint

pc_lotto = []
my_lotto = []
for _ in range(6):
    random_lotto = randint(1, 49)
    user_lotto = int(input("enter number: "))
    pc_lotto.append(random_lotto)
    my_lotto.append(user_lotto)
print(sorted(pc_lotto))
print(sorted(my_lotto))

differences = set(pc_lotto) & set(my_lotto)

print(f"Your win number is {differences}")