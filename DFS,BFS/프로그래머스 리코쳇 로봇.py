from collections import deque
def solution(board):
    dx = [1,0,-1,0]
    dy = [0,-1,0,1]
    r,c = len(board), len(board[0])
    visited = set()

    # 출발 좌표 뽑기
    for i in range(r):
        for j in range(c):
            if board[i][j] == 'R':
                start = (i,j,0)
                visited.add((i,j))
    q = deque([start])

    # 미끄러진 위치 계산
    def move(x, y, ax, ay):
        while 0 <= x+ax < r and 0<= y+ay < c and board[x+ax][y+ay] != 'D':
            x += ax
            y += ay
        return x, y

    # BFS
    def BFS(q):
        while q:
            x, y, cnt = q.popleft()
            for k in range(4):
                nx, ny = move(x, y, dx[k], dy[k])
                if board[nx][ny] == 'G':
                    return cnt + 1
                if (nx,ny) not in visited:
                    q.append((nx,ny,cnt+1))
                    visited.add((nx,ny))
        return -1

    return BFS(q)
