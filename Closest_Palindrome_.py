def pan(n):
    t=n
    r=0
    while(n):
        r=r*10+(n%10)
        n//=10
    if(t==r):
        return 1
    else:
        return 0
n=int(input())
t=n
c,s,i=0,0,1
while(1):
    n=n+i
    c+=1
    if(pan(n)):
        break
while(t):
    t=t-1
    s+=1
    if(pan(t)):
        break
if(s<c):
    print(t)
elif(c<s):
    print(n)
else:
    print(t,n)