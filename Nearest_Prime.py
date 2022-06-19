x=int(input())
for y in range(x):
    n=int(input())
    t=n
    c=0
    s=0
    while(n>0):
        c+=1
        for i in range(2,int(n**0.5)+1):
            if(n%i==0):
                break
        else:
            #print(n)
            break
        n-=1
    while(t>0):
        s+=1
        for i in range(2,int(t**0.5)+1):
            if(t%i==0):
                break
        else:
            #print(t)
            break
        t+=1
    if(s>=c):
        print(n)
    else:
        print(t)