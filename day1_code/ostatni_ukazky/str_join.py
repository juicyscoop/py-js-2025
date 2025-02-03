my_list = ['A', 'long', 'time', 'ago,', 'in', 'a', 'galaxy', 'far,', 'far', 'away...']
my_str = " ".join(my_list)
print(my_str)

apple_data = [1, "Apple Inc.", 1000, "Tim Cook"]

stringified = [str(i) for i in apple_data]

print(f"stringified: {stringified}")

apple_csv_data = ",".join(stringified)

print(f"apple_csv_data: {apple_csv_data}")


