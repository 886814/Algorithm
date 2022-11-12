import sys
from collections import deque
n = int(input())
q = deque([])
for _ in range(n):
    s = sys.stdin.readline().split()
    if len(s) == 2:
            q.append(int(s[1])) if s[0] == "push_back" else q.appendleft(int(s[1]))
    elif s[0] == 'pop_front':
        print(q.popleft()) if q else print(-1)
    elif s[0] == 'pop_back':
        print(q.pop()) if q else print(-1)
    elif s[0] == 'size':
        print(len(q))
    elif s[0] == 'empty':
        print(0) if q else print(1)
    elif s[0] == 'front':
        print(q[0]) if q else print(-1)
    elif s[0] == 'back':
        print(q[-1]) if q else print(-1)
