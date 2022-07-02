def pan(n):
    t=n
    s=0
    while(n):
        s=s*10+(n%10)
        n//=10
    if(t==s):
        return 1
    return 0
def prime(n):
    if(n==1):
        return 0
    for i in range(2,int(n**0.5)+1):
        if(n%i==0):
            return 0
    return 1
n=int(input())
while(1):
    n+=1
    if(prime(n) and pan(n)):
        print(n)
        break
    