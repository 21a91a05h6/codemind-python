s=input()
for i in s:
    c=0
    for j in s:
        if(i==j):
            c+=1
    if(c==1):
        print(i)
        break
else:
    print('-1')