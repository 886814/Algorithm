from collections import deque
import sys

def D(x):
    return (2*x) % 10000

def S(x):
    return x-1 if x != 0 else 9999

def L(x):
    return x%1000*10 + x//1000

def R(x):
    return x%10*1000 +  x//10

input = sys.stdin.readline
t = int(input())
for _ in range(t):
    visited = dict()
    a,b = map(int,input().split())
    q = deque([(a,"")])
    visited = [False] * 10000
    visited[a] = True
    
    while q:
        s,c = q.popleft()
        visited[s] = True
        if s == b:
            print(c)
            break
        else:
            D_, S_, L_, R_ = D(s), S(s), L(s), R(s)
            if not visited[D_]:
                q.append((D_ , c + "D"))
                visited[D_] = True
            if not visited[S_]:
                q.append((S_ , c + "S"))
                visited[S_] = True
            if not visited[L_]:
                q.append((L_ , c + "L"))
                visited[L_] = True
            if not visited[R_]:
                q.append((R_ , c + "R"))
                visited[R_] = True
