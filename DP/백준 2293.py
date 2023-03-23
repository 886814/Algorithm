import sys
input = sys.stdin.readline
n,k = map(int,input().split())
dp = [1] + [0]*k
coin = [1] + [int(input()) for _ in range(n)]
for i in range(1,n+1):
    for j in range(coin[i],k+1):
        dp[j] = dp[j] + dp[j-coin[i]]
print(dp[k])