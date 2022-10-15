n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
ans = 25000001
a.sort()
b.sort(reverse = True)
s = 0
for x,y in zip(a,b):
    s += x*y
print(s)