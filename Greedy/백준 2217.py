n = int(input())
nums = sorted([int(input()) for _ in range(n)], reverse = True)
print(max([nums[i-1]*i for i in range(1,n+1)]))
