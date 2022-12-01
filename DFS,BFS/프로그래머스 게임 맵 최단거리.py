from collections import deque
def solution(maps):
    n, m = len(maps[0]),len(maps)
    dp = [[0]* n for _ in range(m)]
    dp[0][0]= 1
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    q = deque([(0,0)])
    while q:
        x,y = q.popleft()
        for k in range(4):
            ax = x + dx[k]
            ay = y + dy[k]
            if ax == m-1 and ay == n-1:
                return dp[x][y] + 1
            if 0 <= ax < m and 0 <= ay < n and maps[ax][ay] and not dp[ax][ay] :
                dp[ax][ay] = dp[x][y] + 1
                q.append((ax,ay))
    return -1