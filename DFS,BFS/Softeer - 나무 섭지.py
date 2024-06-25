from collections import deque
n,m = map(int,input().split())
a = [list(input()) for _ in range(n)]
visited = [[0] * m for _ in range(n)]
visited_g =[[0] * m for _ in range(n)]
dx = [1,0,-1,0]
dy = [0,1,0,-1]
q = deque([])
ghost = deque([])

for i in range(n):
    for j in range(m):
        if a[i][j] == 'N':
            q.append((i,j))
        if a[i][j] == 'G':
            ghost.append((i,j))
        if a[i][j] == 'D':
            d_x, d_y = (i,j)

# 남우
while q:
    x,y = q.popleft()
    for k in range(4):
        ax = x + dx[k]
        ay = y + dy[k]
        if 0 <= ax < n and 0 <= ay < m:
            if visited[ax][ay] == 0 and a[ax][ay] != '#' and a[ax][ay] != 'G':
                q.append((ax, ay))
                visited[ax][ay] = visited[x][y] + 1
#유령
while ghost:
    x,y = ghost.popleft()
    for k in range(4):
        ax = x + dx[k]
        ay = y + dy[k]
        if 0 <= ax < n and 0 <= ay < m:
            if visited_g[ax][ay] == 0 and a[ax][ay] != 'G':
                ghost.append((ax, ay))
                visited_g[ax][ay] = visited_g[x][y] + 1

if visited[d_x][d_y] != 0 and (visited[d_x][d_y] < visited_g[d_x][d_y]):
    print('yes')
else:
    print('no')