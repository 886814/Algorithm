from collections import deque
from heapq import heappop, heappush

def move_numbers(cap, k, score, m):
    set_ = set()
    upper = deque()
    lower = []

    for i, sc in enumerate(score):
        if sc > k:
            upper.append([sc, i])
        else:
            heappush(lower, [sc, i])

    if len(upper) < m:
        return 0

    while len(upper) >= m:
        if not lower:
            return -1

        upper_e1 = upper[-1]
        lower_e1 = heappop(lower)
        diff = min(upper_e1[0] - k, k - lower_e1[0])

        if diff == 0:
            return -1

        set_.add(upper_e1[1])
        set_.add(lower_e1[1])

        upper_e1[0] -= diff
        lower_e1[0] += diff

        if upper_e1[0] == k:
            upper.pop()

        if lower_e1[0] < k:
            heappush(lower, lower_e1)

    return len(set_)

print(move_numbers(cap, k, score, m))
