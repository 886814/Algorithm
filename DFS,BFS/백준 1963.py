import sys
from collections import deque
ch=[True]*(10000)
for i in range(2, 100):
    if ch[i]:
        for j in range(i+i, 10000, i):
            if ch[j]:
                ch[j] = False
oper = [1000,100,10,1,-1000,-100,-10,-1] 
t = int(input())
for _ in range(t):
    visited = [False] * 10000
    x,y = map(int,sys.stdin.readline().split())
    q = deque([(x,0)])
    visited[x] = True
    while q:
        temp, cnt = q.popleft()
        if temp == y:
            print(cnt)
            break
        for k in oper:
            l = 4-len(str(k)[1:]) if k < 0 else 4-len(str(k))
            for i in range(1,10):
                new = temp + i*k
                if new > 9999 or new < 1000:
                    continue
                elif str(new)[l-1] != str(temp)[l-1]:
                    continue
                if ch[new] and not visited[new]:
                    q.append((new,cnt+1))
                    visited[new] = True
    else:
        print('impossible')