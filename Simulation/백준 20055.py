from collections import deque
n,k = map(int,input().split())
q = list(map(int,input().split()))
q = deque([[x,0] for x in q])
cnt = 0

while True:
    q.rotate(1)
    q[n-1][1] = 0

    for i in range(n-2,-1,-1):
        if q[i+1][1] == 0 and q[i+1][0] > 0 and q[i][1] == 1:
            q[i+1][1] = 1
            q[i+1][0] -= 1
            q[i][1] = 0
    q[n-1][1] = 0

    if q[0][0] > 0:
        q[0][0] -= 1
        q[0][1] = 1
    cnt += 1
    
    if len([x for x in q if x[0] == 0]) >= k:
        break

print(cnt)