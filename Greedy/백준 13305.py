n = int(input())
leng = list(map(int,input().split()))
liter = list(map(int,input().split()))
res = 0
for i in range(n-1):
    if liter[i] < liter[i+1]:
        liter[i+1] = liter[i]
    res += liter[i] * leng[i]

print(res)
print(sum([x*y for x,y in zip(leng,liter)]))