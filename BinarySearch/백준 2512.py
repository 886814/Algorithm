n = int(input())
budgets = list(map(int,input().split()))
total = int(input())
budgets.sort()
lt,rt = 0, budgets[-1]
ans = 0
while lt<=rt:
    mid = (lt+rt)//2
    sum_ = sum([mid if x >= mid else x for x in budgets])
    if sum_ <= total:
        ans = mid
        lt = mid+1
    else:
        rt = mid-1
print(ans)
