n = int(input())
a = [[0]*100 for _ in range(100)]
for i in range(n):
    x,y = map(int,input().split())
    for j in range(x, x+10):
        for k in range(y, y+10):
            a[j][k] = 1
print(sum([sum(x) for x in a]))