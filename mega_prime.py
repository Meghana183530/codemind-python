from math import *
def isprime(n):
    if n==0 or n==1:
        return False
    sq=int(sqrt(n))
    for j in range(2,sq+1):
        if n%j==0:
            return False
    return True
n=int(input())
c=0
a=n
if isprime(n):
    while n:
        r=n%10
        n=n//10
        if isprime(r):
            c+=1
    if c==len(str(a)):
        print("Mega Prime")
    else:
        print("Not Mega Prime")
else:
    print("Not Mega Prime")