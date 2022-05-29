def findSum(s):
    Sum=0
    for ch in s:
        if(ch.isdigit()==True):
            z=int(ch)
            Sum=Sum+z
    return Sum
s=str(input())
print(findSum(s))