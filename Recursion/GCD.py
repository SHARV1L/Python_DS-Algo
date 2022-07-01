import math as m

def gcd(n1, n2):
    rem = n1%n2
    if rem != 0:
        return gcd(n2, rem)
    if rem == 0:
        return n2

num1 = int(input('Enter the first number- '))
num2 = int(input('Enter the second number- '))
num1 = m.fabs(num1)
num2 = m.fabs(num2)
if num1>num2:
    print(gcd(num1, num2)) 
if num1<num2:
    print(gcd(num2, num1))
