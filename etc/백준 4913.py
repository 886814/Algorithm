ch=[0]*(1000001)
X,Y = [], []
for i in range(2, 1000001):
    if ch[i]==0:
        X.append(i)
        if (i-1) % 4 == 0 or i == 2:
            Y.append(i)
        for j in range(i, 1000001, i):
            ch[j]=1
            
while True:
    l,u = map(int,input().split())
    if l == -1 and u == -1:
        break
    x = len([k for k in X if k >=l and k <= u])
    y = len([j for j in Y if j >=l and j <= u])
    print(l,u,x,y)
