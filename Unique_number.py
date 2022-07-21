n=int(input())
t=n
x=0
k=0
while(n):
    d=n%10
    n=n//10
    x+=1
    a=t
    c=0
    while(a):
        h=a%10
        a=a//10
        if(h==d):
            c+=1
    if(c==1):
        k+=1
if(k==x):
    print('Unique Number')
else:
    print('Not Unique Number')