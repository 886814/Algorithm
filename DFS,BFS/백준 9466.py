import sys
sys.setrecursionlimit(2500000)

def DFS(x,q):
    global check, ans
    check[x] = 1
    q.append(x)
    next_ = students[x]
    
    if check[next_]:
        if next_ in q:
            ans += q[q.index(next_):]
            return
    else:
        DFS(next_,q)
    
t = int(input())
for _ in range(t):
    n = int(input())
    ans = []
    check = [0] * (n+1)
    students = [0] + list(map(int,input().split()))
    for i in range(1,n+1):
        if not check[i]:
            q = []
            DFS(i,q)
    print(n-len(ans))