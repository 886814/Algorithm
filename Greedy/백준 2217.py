n = int(input())
weights =[0] + [int(input()) for _ in range(n)]
weights.sort()
ans = 0
for i in range(1,n+1):
    ans = max(ans, weights[n-i+1]*i)
print(ans)