def sq(n):
    for i in range(1,int(n**0.5)+1):
        if(i**2==n):
            return True
    else:
        return False
n=int(input())
a=list(map(int,input().split()))
s=0
for i in range(0,n):
    if(sq(a[i])):
        s+=a[i]
print(s)