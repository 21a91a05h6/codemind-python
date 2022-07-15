s=input()
ch=input()
if ch in s:
    print(True)
    for i in range(0,len(s)):
        if(ch==s[i]):
            print(i)
            break
else:
    print(False)