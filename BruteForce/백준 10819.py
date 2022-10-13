import itertools as it
n = int(input())
nums = list(map(int,input().split()))
ans = 0
for x in it.permutations(nums,n):
    sum_ = 0
    for i in range(0,n-1):
        sum_ += abs(x[i] - x[i+1])
    ans = max(ans, sum_)
print(ans)