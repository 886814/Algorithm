from collections import deque
n, m = map(int,input().split())
degree = [0] * (n+1)
graph = [[0]*(n+1) for _ in range(n+1)]
q =deque([])
for i in range(m):
    x,y = map(int,input().split())
    degree[y] += 1
    graph[x][y] = 1
for i in range(1, n+1):
    if degree[i] == 0:
        q.append(i)
while q:
    x = q.popleft()
    print(x, end = ' ')
    for i in range(1,n+1):
        if graph[x][i]:
            degree[i] -= 1
            if degree[i] == 0:
                q.append(i)
