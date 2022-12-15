from collections import deque

def D(x):
    return str((2*int(x)) % 10000)

def S(x):
    return str(int(x)-1) if int(x) != 0 else "9999"

def L(x):
    return x[1:] + x[0]

def R(x):
    return x[-1] + x[:2]

t = int(input())
for _ in range(t):
    visited = []
    a,b = input().split()
    a,b = a.zfill(4), b.zfill(4)
    q = deque([(a,"")])
    while q:
        s,c = q.popleft()
        s = s.zfill(4)
        visited.append(c)
        if s == b:
            print(c)
            break
        else:
            if c + "D" not in visited:
                q.append((D(s), c + "D"))
                visited.append(c + "D")
            if c + "S" not in visited:
                q.append((S(s), c + "S"))
                visited.append(c + "S")
            if c + "L" not in visited:
                q.append((L(s), c + "L"))
                visited.append(c + "L")
            if c + "R" not in visited:
                q.append((R(s), c + "R"))
                visited.append(c + "R")



0001 0002 0004 0003 0006 00012
