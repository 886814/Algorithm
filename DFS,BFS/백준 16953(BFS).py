from collections import deque
a,b = map(int,input().split())
q = deque([(a,1)])

while q:
    now, cnt = q.popleft()
    if now  == b:
        print(cnt)
        break
    for next_ in (now * 2, now * 10 + 1):
        if next_ <= b:
            q.append((next_,cnt+1))
else:
    print(-1)