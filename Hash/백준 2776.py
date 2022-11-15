import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    m = int(input())
    b = list(map(int,input().split()))
    dic = {}
    for i in a:
        dic[i] = 1
    for x in b:
        print(1) if dic.get(x,0) else print(0)