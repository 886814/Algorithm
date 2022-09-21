n,m = map(int,input().split())
a = sorted(list(map(int,input().split())))
lt,rt = a[0],a[-1]
while lt<=rt:
    mid = (rt+lt)//2
    temp = sum([x-mid for x in a if x > mid])
    if temp >= m:
        lt = mid + 1
    else:
        rt = mid -1
print(rt)