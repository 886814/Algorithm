import sys
n = int(sys.stdin.readline())
a = sorted(list(map(int, sys.stdin.readline().split())))
num = a[0] + a[n-1]
ans = [a[0],a[-1]]
lt = 0
rt = n-1
while lt < rt:
    mid = a[lt] + a[rt]
    if mid == 0 :
        print(a[lt], a[rt])
        break
    if abs(num) > abs(mid):
        num = mid
        ans = [a[lt],a[rt]]
    elif mid >= 0:
        rt -= 1
    else:
        lt += 1
else:
    print(*ans)