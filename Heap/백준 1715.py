import heapq
n = int(input())
q = [int(input()) for _ in range(n)]
heapq.heapify(q)
sum_ = 0
while len(q) > 1:
    tmp = heapq.heappop(q) + heapq.heappop(q)
    sum_ += tmp
    heapq.heappush(q, tmp)
print(sum_)