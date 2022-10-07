n,l = map(int,input().split())
for i in range(l,101):
    a = (2*n - i*i + i)/2/i
    if a < 0 or int(a) != a:
        continue
    else:
        sum_ = sum([a+x for x in range(i)])
        if sum_ == n:
            print(" ".join([str(int(a+x)) for x in range(i)]))
            break
else:
    print(-1)
