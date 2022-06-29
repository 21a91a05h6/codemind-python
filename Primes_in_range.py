def prime(n):
    if n==1:
        return 0
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return 0
    else:
        return 1

x=int(input())
y=int(input())
c=0
for i in range(x,y+1):
    if prime(i):
        c+=1
print(c)
