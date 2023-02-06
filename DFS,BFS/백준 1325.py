import sys
from collections import deque

def BFS(j,trust):
    q = deque([j])
    visited = [0] * (n+1)
    visited[j] = 1
    cnt = 1
    while q:
        now_ = q.popleft()
        for next_ in trust[now_]:
            if visited[next_] == 0:
                visited[next_] = 1
                cnt += 1
                q.append(next_)
    return cnt

input = sys.stdin.readline
n,m = map(int,input().split())
trust = {}
for i in range(1,n+1):
    trust[i] = []
for _ in range(m):
    a,b = map(int,input().split())
    trust[b].append(a)

res = [0] * (n+1)
max_ = 0
for j in range(1,n+1):
    res[j] = BFS(j,trust)
    max_ = max(max_, res[j])

for x in range(len(res)):
    if res[x] == max_:
        print(x, end = " ")