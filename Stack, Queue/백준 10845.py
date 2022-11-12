import sys
from collections import deque
n = int(input())
q = deque([])
for _ in range(n):
    s = sys.stdin.readline().split()
    if len(s) == 2:
        q.append(int(s[1]))
    elif s[0] == 'pop':
        print(q.popleft()) if q else print(-1)
    elif s[0] == 'size':
        print(len(q))
    elif s[0] == 'empty':
        print(0) if q else print(1)
    elif s[0] == 'front':
        print(q[0]) if q else print(-1)
    elif s[0] == 'back':
        print(q[-1]) if q else print(-1)
