


l = [i for i in range(10) if i % 3 == 0]
print(l)
l = [i if i % 3 == 0 else "hello" for i in range(10)]
print(l)

l[0] = "nova_hodnota"

a = tuple(i for i in l)

print(a)

a[0] = "nova hodnota"