s=str(input())
c=0
a=[]
for i in range(0,len(s)):
    if(s[i]==' '):
        a.append(c)
        c=0
    c+=1
if(len(a)==0):
    print(c)
else:
    print(min(a))