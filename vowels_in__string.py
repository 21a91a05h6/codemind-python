s=input()
a='aeiouAEIOU'
b=''
c=0
for i in s:
    if i in a and i not in b:
        b=b+i
        c+=1
if(c==0):
    print('-1')
else:
    for i in b:
        print(i,end=' ')