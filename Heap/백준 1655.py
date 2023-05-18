import heapq
lh, rh = [], []
heapq.heapify(lh)
heapq.heapify(rh)
n = int(input())
for i in range(n):
    num = int(input())
    if len(rh) == len(lh):
        heapq.heappush(lh, (-num, num))
    else:
        heapq.heappush(rh, (num, num))
    
    if rh and lh[0][1] > rh[0][1]:
        l = heapq.heappop(lh)[1]
        r = heapq.heappop(rh)[1]
        heapq.heappush(lh, (-r, r))
        heapq.heappush(rh, (l, l))
    
    print(lh[0][1])