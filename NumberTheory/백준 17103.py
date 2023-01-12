import sys
input = lambda: sys.stdin.readline().rstrip()

n = 1000000
sieve = [1]*(n+1)
sieve[4::2] = [0]*((n-4)//2+1)
for i in range(3,int(n**.5)+1,2):
    sieve[i*i::2*i] = [0]*((n-i*i)//(i*2)+1)
primes = [2] + [i for i in range(3,n+1,2) if sieve[i]]

def gbcnt(param:int):
    ans = 0
    for p in primes:
        if 2*p > param:
            return ans
        if sieve[param-p]:
            ans += 1

for _ in range(int(input())):
    print(gbcnt(int(input())))
