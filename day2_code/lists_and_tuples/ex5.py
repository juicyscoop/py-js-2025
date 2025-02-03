
def mean(seznam_cisel):
    return sum(seznam_cisel)/len(seznam_cisel)
print(mean([1,2,3,4]))

def mean_manual(seznam_cisel):
    length = 0
    sumx = 0
    for i in seznam_cisel:
        sumx += i
        length += 1
    return sumx/length
print(mean_manual([1,2,3,4]))

def mean_vojtech(seznam_cisel):
        sumx = 0
        for i in seznam_cisel:
            sumx += i
        result = sumx / len(seznam_cisel)
        return result
print(mean_vojtech([1,2,3,4]))
