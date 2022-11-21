import sys
input = sys.stdin.readline

def DFS(x,l):
    if l == 4:
        print(1)
        exit()
        return 
    else:
        for t in dic[x]:
            if not visited[t]:
                visited[t] = 1
                DFS(t,l+1)
                visited[t] = 0

n,m = map(int,input().split())
dic = dict()
for i in range(n):
    dic[i] = []

for j in range(m):
    p,c = map(int,input().split())
    dic[p].append(c)
    dic[c].append(p)

for k in range(n):
    visited = [0] * (n+1)
    visited[k] = 1
    DFS(k,0)
else:
    print(0)