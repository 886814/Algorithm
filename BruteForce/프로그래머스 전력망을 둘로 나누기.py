from itertools import combinations
from collections import deque

def solution(n, wires):
    ans = n
    for combi in combinations(wires,len(wires)-1):
        hash = {i:[] for i in range(n+1)}
        for relation in combi:
            x,y = relation
            hash[x].append(y)
            hash[y].append(x)

        visited = [0]* (n+1)

        start = combi[0][0]
        q = deque(hash[start])
        visited[start] = 1
        while q:
            tmp = q.popleft()
            if not visited[tmp]:
                visited[tmp] = 1
                for i in range(len(hash[tmp])):
                    if not visited[hash[tmp][i]]:
                        q.append(hash[tmp][i])
        cnt = sum(visited)
        ans = min(ans, abs(n-2*cnt))

    return ans