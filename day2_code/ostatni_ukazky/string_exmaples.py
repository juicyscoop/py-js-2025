
"""
s = "Harry"
for i in s:
    print(i, end="")
"""

# Formatovani stringu:
x = "Hello"
fs = f"{x}"

fs2 = "{data_value} - {data_value2} - {data-value3}".format(
    data_value=x,
    data_value2=y,
    data_value3=y
)

print(fs2)

hobbits = ("Frodo", "Sam",
           "Merry", "Pippin")
desc = ("Hobbits in LOTR: %i, %s, %s" +
        " and %s.") % hobbits
print(desc)
