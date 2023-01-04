ch=[True]*(10000001)
ch[1] = False
for i in range(2, 100001):
    if ch[i]:
        for j in range(i+i, 10000001, i):
            if ch[j]:
                ch[j] = False
                
n = int(input())
i = n
while i >=n:
    if ch[i] and i == int(str(i)[::-1]):
        print(i)
        break
    i += 1