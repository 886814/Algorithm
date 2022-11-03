import sys
n = int(input())
nums = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]
nums.sort(key = lambda x: (x[0],x[1]))
for x,y in nums:
    print(x,y)