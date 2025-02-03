def list_keys(d):
    list_case = [i for i in d]
    return list_case

def list_keys_2(d):
    list_case = d.keys()
    return list_case

slovnik = {
    "a": 1,
    "b": 2
}

listed_keys = list_keys_2(slovnik)

print(listed_keys)
print(type(listed_keys))

for i in list_keys_2(slovnik):
    print(i)

