from collections import deque
import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    convi = []
    ans = 'sad'
    n = int(input())
    x_s, y_s = map(int,input().split())
    q = deque([(x_s, y_s)])
    visited = [(x_s,y_s)]
    for _ in range(n):
        a, b = map(int,input().split())
        convi.append((a,b))
    x_r, y_r = map(int,input().split())
    
    while q:
        x,y = q.popleft()
        tmp = (abs(x_r-x) + abs(y_r-y)) / 50
        if tmp <= 20 :
            ans = 'happy'
            break
        for c in convi:
            ax, ay = c
            if c not in visited:
                dis = abs(ax-x) + abs(ay-y)
                mod = dis / 50
                if mod <= 20:
                    q.append((ax,ay))
                    visited.append((ax,ay))

    print(ans)