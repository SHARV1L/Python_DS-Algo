def SOD(n):
    if n in [0,1,2,3,4,5,6,7,8,9]:
        return n
    else:
        return int(n%10) + SOD(int(n/10))

s = int(input('Enter the number n- '))
print(SOD(s))
