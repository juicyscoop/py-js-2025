

def sumup(seznam_cisel):
    res = 0
    for i in seznam_cisel:
        res += i
    return res

soucet = sumup(seznam_cisel=[1,2,3,4])
soucet2 = sum(
    [1,2,3,4]
)

print(soucet)
print(soucet2)

# return sum([i for i in numbers])
# print(sum([1,2,3,4,5]))