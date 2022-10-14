a=int(input())
is_prime=True
for i in range(2,int(a**0.5)+1):
    if a%i==0:
        is_prime=False
        break
if is_prime==True:
    print("prime")
else:
    print("not a prime")