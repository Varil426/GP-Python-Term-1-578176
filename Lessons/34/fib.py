from pprint import pprint

fib_dict = {0:0,1:1}

def fibonacci(n):
    if n in fib_dict:
        return fib_dict[n]
    else:
        result = fibonacci(n-1) + fibonacci(n-2)
        fib_dict[n] = result
        return result
    
fibonacci(20)
pprint(fib_dict)
fibonacci(34)
pprint(fib_dict)