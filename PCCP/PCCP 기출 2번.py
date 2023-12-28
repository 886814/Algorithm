from collections import deque
def solution(land):
    n, m = len(land), len(land[0])
    visited = [[0] * m for _ in range(n)]
    ans = 0
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    q = deque([])
    sum_ = dict()
    s = 1
    for i in range(n):
        for j in range(m):
            if land[i][j] == 1 and visited[i][j] == 0:
                cnt = 1
                q.append((i,j))
                visited[i][j] = s
                while q:
                    x,y = q.popleft()
                    for k in range(4):
                        ax = x + dx[k]
                        ay = y + dy[k]
                        if 0 <= ax < n and 0 <= ay < m and visited[ax][ay] == 0 and land[ax][ay] == 1:
                            q.append((ax,ay))
                            visited[ax][ay] = s
                            cnt += 1
                sum_[s] = cnt
                s += 1

    for i in range(m):
        temp = 0
        check = [False] * (s+1)
        for j in range(n):
            if visited[j][i] != 0 and not check[visited[j][i]]:
                temp += sum_[visited[j][i]]
                check[visited[j][i]] = True
        ans = max(ans, temp)
    return ans