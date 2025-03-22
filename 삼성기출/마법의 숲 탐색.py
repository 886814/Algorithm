from collections import deque
r,c,k = map(int,input().split())
golems = [list(map(int,input().split())) for _ in range(k)]
forest = [[0]*(c) for _ in range(r)]
ans = 0
new_r = r + 4
new_c = c + 2
map_ = [0] * (k+1)

def make_forest():
    new_forest = [[-1] * new_c for _ in range(new_r)]

    for i in range(r):
        for j in range(c):
            new_forest[i + 3][j + 1] = forest[i][j]

    for i in range(3):
        for j in range(1, c + 1):
            new_forest[i][j] = 0

    return new_forest

def BFS(x,y):
    global ans
    q = deque([(x,y)])
    res = 0
    visited = [[0]*(c+2) for _ in range(r+4)]
    visited[x][y] = 1
    dx = [1,0,-1,0]
    dy = [0,1,0,-1]
    while q:
        x,y = q.popleft()
        for k in range(4):
            ax = x + dx[k]
            ay = y + dy[k]
            if visited[ax][ay] == 0 and (new_forest[ax][ay] > 0 or new_forest[ax][ay] == -2):
                if (
                        new_forest[ax][ay] == new_forest[x][y]
                        or (new_forest[ax][ay] != new_forest[x][y] and new_forest[ax][ay] == -2 and map_.index((ax,ay)) == new_forest[x][y])
                        or (new_forest[ax][ay] != new_forest[x][y] and new_forest[x][y] == -2)
                        ):
                    visited[ax][ay] = 1
                    q.append((ax, ay))
                    res = max(res, ax)
    ans += res-2

def check(x,y):
    if 4 <= x and new_forest[x][y] == 0 and new_forest[x-1][y] == 0 and new_forest[x+1][y] == 0 and new_forest[x][y-1] == 0 and new_forest[x][y+1] == 0:
        return True
    return False

def fill(x, y, d, idx):
    global new_forest, map_ 
    dir_map = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    new_forest[x][y] = idx
    for i, (dx, dy) in enumerate(dir_map):
        nx, ny = x + dx, y + dy
        if i == d:
            new_forest[nx][ny] = -2
            map_[idx] = (nx,ny)
        else:
            new_forest[nx][ny] = idx

def move(x,y,d):
    # 처음 시작
    if x == 1 and new_forest[x+2][y] == 0:
        x += 1
    while True:
        # 아래로 한칸
        if new_forest[x+2][y] == 0 and new_forest[x+1][y-1] == 0 and new_forest[x+1][y+1] == 0:
            x += 1
        # 왼쪽 회전
        elif new_forest[x+1][y-1] == 0 and new_forest[x-1][y-1] == 0 and new_forest[x][y-2] == 0 and new_forest[x+1][y-2] == 0 and new_forest[x+2][y-1] == 0:
            d = (d - 1) % 4
            x += 1
            y -= 1
        # 오른쪽 회전
        elif new_forest[x+1][y+1] == 0 and new_forest[x-1][y+1] == 0 and new_forest[x][y+2] == 0 and new_forest[x+1][y+2] == 0 and new_forest[x+2][y+1] == 0:
            d = (d + 1) % 4
            x += 1
            y += 1
        else:
            return x,y,d
    return x,y,d

new_forest = make_forest()
for idx, golem in enumerate(golems, start=1):
    col, d = golem
    x,y,d = move(1, col, d)
    if not check(x,y):
        new_forest = make_forest()
        map_ = [0] * (k+1)
        continue
    fill(x,y,d,idx)
    BFS(x,y)
    
print(ans)