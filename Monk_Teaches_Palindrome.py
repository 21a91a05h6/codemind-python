t=int(input())
for i in range(t):
    s=input()
    a=s[::-1]
    if(a==s):
        print("YES",end=' ')
        if(len(s)%2==0):
            print('EVEN')
        else:
            print("ODD")
    else:
        print("NO")