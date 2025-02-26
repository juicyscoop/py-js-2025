import time

def timing(func):
    """
    A decorator to measure execution time of wrapped function
    """
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"\n Execution time of func: {end - start}\n")
        return result
    return wrapper

@timing
def addition(a,b):
    return a+b


if __name__ == "__main__":
    addition(10,20)
