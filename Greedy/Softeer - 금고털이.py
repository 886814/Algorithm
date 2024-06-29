w, n = 100, 2
#jewelry = [list(map(int,input().split())) for _ in range(n)]
jewelry = [[70, 2], [90, 1]]
jewelry.sort(key=lambda x: -x[1])
res = 0
for jewel in jewelry:
    s, v = jewel
    if w >= s:
        w -= s
        res += s * v
    else:
        res += w*v
        break