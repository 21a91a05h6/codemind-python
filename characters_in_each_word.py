s=str(input())
c=0
a=0
for i in range(0,len(s)):
    c+=1
    if(s[i]==' '):
        print(c-1,end=' ')
        c=0
    elif(i==len(s)-1):
        print(c,end=' ')