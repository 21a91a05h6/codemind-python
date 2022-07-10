n=int(input())
x=0
y=1
while(1):
    if n<x:
        if(abs(n-y)>abs(x-n)):
            print(x)
        elif(abs(n-y)==abs(x-n)):
            print(y,x)
        else:
            print(y)
        break
    t=x
    x=x+y
    y=t