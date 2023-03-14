import sys
input = sys.stdin.readline
n = int(input())
nums = [0] * (10001)
for i in range(n):
    x = int(input())
    nums[x] += 1
for j in range(10001):
    for k in range(nums[j]):
        sys.stdout.write(str(j)+'\n')
