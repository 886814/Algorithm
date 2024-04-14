n = int(input())
a = [[0] + list(map(int,input().split()))+[0] for _ in range(n)]
a.insert(0,[0]*(n+2))
a.append([0]*(n+2))
cnt = 0

for i in range(1, n+1):
    for j in range(1, n+1):
        if a[i][j]>a[i][j-1] and a[i][j]>a[i][j+1] and a[i][j]>a[i-1][j] and a[i][j]>a[i+1][j]:
            cnt += 1

print(cnt)