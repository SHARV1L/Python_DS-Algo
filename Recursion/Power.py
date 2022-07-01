def power(n, x):
    assert n>0 and x>=0, 'The base condition has to be positive and power can be zero or greater'
    if x == 0:
        return 1
    if x == 1:
        return n
    return n * power(n, x-1)


num = int(input('Enter the base number- '))
p = int(input('Enter the exponent number- '))
print(power(num, p)) 