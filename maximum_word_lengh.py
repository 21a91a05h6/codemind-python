s=str(input())
c=0
a=[]
for i in range(0,len(s)):
    c+=1
    if(s[i]==' '):
        a.append(c-1)
        c=0
    elif(i==len(s)-1):
        a.append(c)
print(max(a))