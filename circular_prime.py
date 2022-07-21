n=int(input())
t=n
c=0
s=0
x=0
for i in range(1,n+1):
    if(n%i==0):
        c+=1
if(c==2):
    while(n!=0):
        d=n%10
        n=n//10
        s=s*10+d
for i in range(1,s+1):
    if(s%i==0):
        x+=1
if(x==2 and c==2):
    print('circular prime')
elif(c==2 and x!=2):
    print('prime but not a circular prime')
elif(c!=2):
    print('not prime')