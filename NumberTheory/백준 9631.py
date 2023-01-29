import math
import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    sum_ = 0
    nums = list(map(int,input().split()))
    n = nums.pop(0)
    for i in range(n-1):
        for j in range(i+1,n):
            sum_ += math.gcd(nums[i], nums[j])
    print(sum_)
