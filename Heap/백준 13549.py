import heapq
n, k = map(int,input().split())
visited = [0] * 100001
q = [(0,n)]
heapq.heapify(q)
while q:
    time,now = heapq.heappop(q)
    if now == k:
        print(time)
        break
    for next_ in (now*2, now-1, now+1):
        if 0 <= next_ <= 100000:
            if visited[next_] == 0:
                if next_ == now *2:
                    heapq.heappush(q,(time,next_))
                    visited[next_] = 1
                else:
                    heapq.heappush(q,(time+1,next_))
                    visited[next_] = 1