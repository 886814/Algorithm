from collections import deque
import sys

def D(x):
    return str((2*int(x)) % 10000)

def S(x):
    return str(int(x)-1) if int(x) != 0 else "9999"

def L(x):
    return x[1:] + x[0]

def R(x):
    return x[-1] + x[:3]

input = sys.stdin.readline
t = int(input())
for _ in range(t):
    visited = dict()
    a,b = input().split()
    a,b = a.zfill(4), b.zfill(4)
    q = deque([(a,"")])
    visited = [False] * 10000
    visited[int(a)] = True
    
    while q:
        s,c = q.popleft()
        visited[int(s)] = True
        s = s.zfill(4)
        if s == b:
            print(c)
            break
        else:
            D_, S_, L_, R_ = D(s), S(s), L(s), R(s)
            if not visited[int(D_)]:
                q.append((D_ , c + "D"))
                visited[int(D_)] = True
            if not visited[int(S_)]:
                q.append((S_ , c + "S"))
                visited[int(S_)] = True
            if not visited[int(L_)]:
                q.append((L_ , c + "L"))
                visited[int(L_)] = True
            if not visited[int(R_)]:
                q.append((R_ , c + "R"))
                visited[int(R_)] = True
