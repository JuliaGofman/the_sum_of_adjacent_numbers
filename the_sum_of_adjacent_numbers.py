s = [int(i) for i in input().split()]
for i in range(0, len(s)):
    if len(s)>1:
        if i != len(s)-1:
            print(s[i-1]+s[i+1], end=' ')
        else:
            print(s[0]+s[-2], end=' ')
    else:
        print(s[0])