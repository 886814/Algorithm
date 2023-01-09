n = list(map(int,input()))
n.sort(reverse=True)
if sum(n) % 3 != 0 or 0 not in n:
    print(-1)
else:
    print("".join(n))
