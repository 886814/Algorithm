s = input().split('-')
ans = sum([int(y) for y in s[0].split('+')])
for i in range(1,len(s)):
    temp = s[i].split('+')
    ans -= sum([int(x) for x in temp])
print(ans)