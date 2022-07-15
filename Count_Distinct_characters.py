s=input()
s=set(list(s))
b=''
for i in s:
    if(ord(i)>=65 and ord(i)<=90):
        b=b+chr(ord(i)+32)
    elif(i!=' '):
        b+=i
b=set(list(b))
print(len(b))