def fibonacci(n):
    assert n>=0 and int(n)==n, "Please enter a positive number"
    if n in [0,1]:
        return n
    else:    
        return fibonacci(n-1) + fibonacci(n-2)

s = int(input('Enter the number - '))
print(fibonacci(s))
