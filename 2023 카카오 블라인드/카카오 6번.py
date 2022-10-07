# 시간초과
from collections import deque
n,m,x,y,r,c,k = 3, 4, 2, 3, 3, 1, 5
a = [[0]*m for _ in range(n)]
a[x-1][y-1] = 'S'
a[r-1][c-1] = 'E'
q = deque([(x-1,y-1,0,"")])
dx = [1,0,-1,0]
dy = [0,-1,0,1]
ans = []
dic = {0:"d",1:"l",2:"u",3:"r"}

while q:
    ax,ay,cnt,s = q.popleft()
    if cnt == k and a[ax][ay] == "E":
        ans.append(s)        
    for t in range(4):
        nx = ax + dx[t]
        ny = ay + dy[t]
        if 0 <= nx < n and 0 <= ny < m:
            if cnt+1 <= k:
                q.append((nx,ny,cnt+1,s+dic[t]))

print("impossible") if len(ans) == 0 else print(sorted(ans)[0])