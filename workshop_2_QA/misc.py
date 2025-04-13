# Workshop 2 Q & A

def func():
    pass


a = func()

print(a)
print(type(a))

a = func


print(a)
print(type(a))

def funkce_ktera_ocekava_funkci(fun: function) -> function:
    print("Udleame neco")
    x = fun()
    print('Udelame neco dalsiho')
    
    def inner():
        return x
    
    return inner

x = funkce_ktera_ocekava_funkci(func)

return_value_of_inner = x()