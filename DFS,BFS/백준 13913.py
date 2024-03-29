from collections import deque
n,k = map(int,input().split())
MAX = 100000
dis = [0] * (MAX+1)
route = [0] * (MAX+1)
dis[n] = 0
dQ = deque()
dQ.append(n)
while dQ:
    now = dQ.popleft()
    if now==k:
        s = []
        temp = now
        for _ in range(dis[now]+1):
            s.append(f"{temp}")
            temp = route[temp]
        break
    for next in (now+1, now-1, 2*now):
        if 0 <= next <= MAX:
            if dis[next]==0:
                dQ.append(next)
                route[next] = now
                dis[next] = dis[now]+1
  
print(dis[k])
print(" ".join(s[::-1]))
