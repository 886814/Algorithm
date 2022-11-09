n = int(input())
a = sorted(list(map(int, input().split())))
for i in range(1, n):
    a[i] += a[i-1]
print(sum(a)) 