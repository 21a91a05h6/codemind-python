s=input()
k=-1
for i in range(len(s)-1,-1,-1):
    if(s[i]==' '):
        k=i
        break
for i in range(0,len(s)):
    if(s[i]==' '):
        c=0
        for j in range(i-1,-1,-1):
            if(s[j]==' '):
                c=1
            if(c==0):
                print(s[j],end='')
            else:
                break
        print(' ',end='')
    if(i==len(s)-1):
        for j in range(len(s)-1,k,-1):
            print(s[j],end='')