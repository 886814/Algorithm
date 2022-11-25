n=int(input())
arr=list(map(int, input().split()))
arr.insert(0,0)
dy=[0]*(n+1)
dy[1]=1

for i in range(1, n+1):
    max_=0
    for j in range(i-1, 0, -1):
        if arr[j]>arr[i] and dy[j]>max_:
            max_=dy[j]
    dy[i]=max_+1

print(max(dy))