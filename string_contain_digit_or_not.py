s=str(input())
digit=0
for chr in s:
    if chr.isdigit():
        digit=digit+1
if digit==0:
    print("Doesn't contain digit")
else:
    print("Contains",digit,"digit")
