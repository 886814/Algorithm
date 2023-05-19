from collections import deque
n,m = map(int,input().split())
a = [list(map(int,input().split())) for _ in range(n)]
visited = [[-1] * m for _ in range(n)]
q = deque([])
dx = [0,1,0,-1]
dy = [1,0,-1,0]

for i in range(n):
    for j in range(m):
        if a[i][j] == 2:
            q.append((i,j))
            s_x, s_y = i ,j
            visited[i][j] = 0
            while q:
                ax, ay = q.popleft()
                for k in range(4):
                    x = ax + dx[k]
                    y = ay + dy[k]
                    if 0 <= x < n and 0 <= y < m and visited[x][y] == -1 and a[x][y] == 1:
                            visited[x][y] = visited[ax][ay] + 1
                            q.append((x,y))
        if a[i][j] == 0:
            visited[i][j] = 0

for r in visited:
    print(*r)