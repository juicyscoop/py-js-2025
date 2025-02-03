
def find_short_words(seznam_slov):
    # return [i for i in seznam_slov if len(i) < 5]
    a = []
    for i in seznam_slov:
        if len(i) < 5:
            a.append(i)
    return a

l = find_short_words(['itsy', 'bitsy', 'spider', 'climbed', 'up', 'the', 'waterspout'])
print(l)
