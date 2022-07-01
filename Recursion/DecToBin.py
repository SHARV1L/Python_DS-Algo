def DecToBin(n):
    if n == 0:
        return 0
    else:
        return n%2 + 10 * DecToBin(int(n/2))

s = int(input('Enter the number - '))
print(DecToBin(s))