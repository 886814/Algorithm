n = int(input())
a = sorted(list(map(int,input().split())))
num = a[0] + a[-1]
ans = [a[0],a[-1]]
lt = 0
rt = n-1
while lt < rt:
    mid = a[lt] + a[rt]
    if mid == 0 :
        break
    if abs(num) > abs(mid):
        num = mid
        ans = [a[lt],a[rt]]
    elif mid > 0:
        rt -= 1
    else:
        lt += 1
else:
    print(*ans)