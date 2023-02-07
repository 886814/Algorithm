import sys
limit_number = 150000
sys.setrecursionlimit(limit_number)

def FIND(v):
    global res
    if len(find[v]) == 0:
        res.append(v)
    else:
        for next_ in find[v]:
            FIND(next_)
                
def DFS(v,tot):
    global max_, res, visited
    if v in tmp:
        max_ = max(max_, tot)
    else:
        for next_, weight in nodes[v]:
            if not visited[next_]:
                visited[next_] = 1
                DFS(next_, tot + weight)
                visited[next_] = 0
                    
n = int(input())
find = {i:[] for i in range(1, n+1)}
nodes = {i:[] for i in range(1, n+1)}
for _ in range(n-1):
    a,b,c = map(int,input().split())
    nodes[a].append((b,c))
    nodes[b].append((a,c))
    find[a].append(b)
        
res = []
for k in find[1]:
    FIND(k)
        
max_ = 0
for start in res:
    tmp = set(res) - {start}
    visited = [0] * (n+1)
    DFS(start,0)
 
print(max_)
