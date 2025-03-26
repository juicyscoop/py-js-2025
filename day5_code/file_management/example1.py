# Prace se soubory


a = open("books.json")
file_content = a.read()
print(file_content)
print(a)
a.close()

# Best practice:
# Context Manager
with open("books.json") as g:
    file_content = g.read()
    print(file_content)







