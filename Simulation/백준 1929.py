m,n=map(int,input().split())
ch=[0]*(n+1)
for i in range(2, n+1):
    if ch[i]==0:
        if i >= m:
            print(i)
        for j in range(i, n+1, i):
            ch[j]=1