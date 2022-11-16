m = int(input())
n = int(input())
ch=[True]*(10001)
for i in range(2, 101):
    if ch[i]:
        for j in range(i+i, 10001, i):
            if ch[j]:
                ch[j] = False
primes = [x for x in range(m,n+1) if ch[x]]
if primes:
    print(sum(primes))
    print(min(primes))
else:
    print(-1)