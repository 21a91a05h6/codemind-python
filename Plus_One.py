n=int(input())
a=list(map(int,input().split()))
s=0
for i in range(len(a)-1,-1,-1):
    s=s*10+a[i]
t=s
r=0
while(t):
    r=r*10+(t%10)
    t=t//10
r=r+1
d=[]

while(r):
    d.append(r%10)
    r=r//10
for i in range(len(d)-1,-1,-1):
    print(d[i],end=' ')