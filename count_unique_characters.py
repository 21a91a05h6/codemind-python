s=input()
a=0
for i in s:
    c=0
    if(ord(i)>=65 and ord(i)<=90):
        i=chr(ord(i)+32)
    for j in s:
        if(i==j):
            c+=1
    if(c==1 and i!=' '):
        a+=1
print(a)