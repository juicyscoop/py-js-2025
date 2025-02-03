s = [1,2,3, 4, 5, 6, 7, 8, 9, 10]

for i in s:
    print(i)

limit = 15
soucet = 0

counter = 0
while (soucet <= limit):
    soucet += s[counter]
    counter += 1

print(f"soucet je {soucet}")



