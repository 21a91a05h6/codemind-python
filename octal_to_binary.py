n=int(input())
c=0
d=0
while(n):
    d=d+(8**c)*(n%10)
    n//=10
    c+=1
print(bin(d)[2:])