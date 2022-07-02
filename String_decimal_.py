n=int(input())
for i in range(0,n):
    s=input()
    c=0
    for j in s:
        if(j=='0' or j=='1' or j=='2' or j=='3' or j=='4' or j=='5' or j=='6' or j=='7' or j=='8' or j=='9'):
            c+=1
    if(c==len(s)):
        print(True)
    else:
        print(False)