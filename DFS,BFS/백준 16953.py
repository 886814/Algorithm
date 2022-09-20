def DFS(x,cnt):
    global b, ans
    if x > b:
        return
    if x == b:
        ans = cnt
        return
    else:
        DFS(x*2,cnt + 1)
        DFS(x*10+1, cnt + 1)

a,b = map(int,input().split())
ans = -1
DFS(a,1)
print(ans)

