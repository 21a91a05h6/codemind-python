n=int(input())
c=k=s=0
while n:
    d=n%10
    n=n//10
    c+=1
    if d%2==0:
        k+=1
    if d%2!=0:
        s+=1
e=s+k
if c==k:
    print("Even")
elif c==s:
    print("Odd")
else:
    print("Mixed")