global x
x = 10

def func():
    global x
    x = 2

func()
print(x)

