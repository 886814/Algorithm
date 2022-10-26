import itertools as it
primes = []
ch=[0]*(1000001)
for i in range(2, 1000001):
    if ch[i]==0:
        primes.append(i)
        for j in range(i, 1000001, i):
            if ch[j] != 1:
                ch[j] = 1

while True:
    n = int(input())
    if n == 0:
        break
    new_primes = [prime for prime in primes if prime < n]
    for x in it.combinations(new_primes,2):
        if sum(x) == n:
            print(f"{n} = {x[0]} + {x[1]}")
            break