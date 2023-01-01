import sys
input = sys.stdin.readline

a = [[0]*15 for _ in range(15)]
a[0] = [i for i in range(1,16)]
for k in range(1,15):
    a[k][0] = 1
    for n in range(1,15):
        a[k][n] = a[k][n-1] + a[k-1][n]

t = int(input())
for _ in range(t):
    k = int(input())
    n = int(input())    
    print(a[k][n-1])