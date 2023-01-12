# DP를 이용한 풀이

def bino_coef(n, r):
    cache = [[0 for _ in range(r+1)] for _ in range(n+1)]

    for i in range(n+1):
        cache[i][0] = 1
    for i in range(r+1):
        cache[i][i] = 1

    for i in range(1, n+1):
        for j in range(1, r+1):
            cache[i][j] = cache[i-1][j] + cache[i-1][j-1]

    return cache[n][r]

n,k = map(int,input().split())
print(bino_coef(n,k) % 10007)

# 조합 정의 풀이

n,k = map(int,input().split())
a, b = 1, 1
for i in range(n,n-k,-1):
    a *= i
for j in range(1,k+1):
    b *= j
ans = a // b
print(ans % 10007)
