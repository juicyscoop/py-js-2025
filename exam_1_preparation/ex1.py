

def normal_function():
    return "A"

def generator_function():
    yield from [1,2,3,4,5]


if __name__ == "__main__":
    a = normal_function
    print(f" a ref: {a}")
    print(f" a return: {a()}")

    b = generator_function
    print(f" b ref: {b}")
    print(f" b yield: {b()}")

    # a = normal_function()
    
    # for i in generator_function():
    #     print(i)

    # a = []
    # for i in range(10):
    #     a.append(i)

    a = [i for i in range(10)]
    a = [
        {
            "a": 1,
        } for i in range(10)
    ]
    a = {i for i in range(10)}
    
    print(a)