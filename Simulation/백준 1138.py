n = int(input())
left = [0] + list(map(int,input().split()))

ans = [0]*(n)
for i in range(1, n+1):
    cnt = left[i]
    for j in range(n):
        if ans[j] == 0:
            if cnt == 0:
                ans[j] = i
                break
            else:
                cnt -= 1

print(*ans)