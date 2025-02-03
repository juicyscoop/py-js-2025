
"""
 def histogram(list_of_numbers):
    for i in list_of_numbers:
       if not isinstance(i, int):
            print(f"Number is not an int: {i}")
            return None
            for _ in range(i):
                print("#", end="")
       print()
"""

# Vojtech
def histogram_vojtech(listing):
    result = []
    for i in listing:
        n = 0
        while n < i:
            result.append("#")
            n += 1
        result.append("\n")
    return "".join(result)

print(histogram_vojtech([1,2,5, 10, 15]))
