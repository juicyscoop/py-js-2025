a = 1
b = a

a = "abc"

a = None


l = [1, 2, 3]
l = list(1, 2, 3)

l = {1, 2, 3}
l = set([1, 2, 3])

dict, list, set, tuple

slovnik = {
    "a": 1,
    "b": 2
}

print(slovnik["a"] + slovnik["b"])




a = [-1, -2, 0, 5, 10]
# Rozdel cisla do katgegorii -> kladne, zaporne, nula

vysledek = {}

for i in a:
    if i > 0:
        if "kladne" not in vysledek:
            vysledek["kladne"] = []
            vysledek["kladne"].append(i)
        else:
            vysledek["kladne"].append(i)