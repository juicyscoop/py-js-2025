from math import floor, ceil

def middle_elements(sequences):
    out = []
    for s in sequences:
        if not s:
            continue
        else:
            delka_sekvence = len(s)
            if delka_sekvence % 2 == 0:
                prostredni_index = int(delka_sekvence/2)
            else:
                prostredni_index = int(floor(delka_sekvence/2))
            out.append(s[prostredni_index])
    return out

class SequenceOfNumbers:
    def __init__(self, start, stop, step):
        self.start = start
        self.stop = stop
        self.step = step

    def __len__(self):
        length = ceil((self.stop - self.start)/self.step)
        # length = 0
        # for i in range(self.start, self.stop, self.step):
        #     length += 1
        return length

    def __getitem__(self, index):

        if not isinstance(index, int):
            raise TypeError("Index must be an integer!")

        if index < 0:
            raise IndexError("Negative indexes are not supported, sorry!")

        nth_element = self.start + index * self.step

        if nth_element >= self.stop:
            raise IndexError("Selected index was too large!")

        return nth_element

        #tracking_index = 0
        #for i in range(self.start, self.stop, self.step):
        #    if tracking_index == index:
        #        return i
        #    else:
        #        tracking_index += 1


