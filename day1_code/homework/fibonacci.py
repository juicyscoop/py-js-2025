def fib(n):
    if n == 1:
        return 0
    if n == 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)
    """
    else:
        s = [0,1]
        for i in range(2, n+1):
            s.append( (s[i-1]) + (s[i-2]) )
        return s
    """

print(fib(1))
print(fib(2))
print(fib(3))
print(fib(4))
print(fib(10))