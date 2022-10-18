def find_prime_nums(n):
    ch=[0]*(n+1)
    primes = []
    for i in range(2, n+1):
        if ch[i]==0:
            ch[i] = 1
            primes.append(i)
            for j in range(i+i, n+1, i):
                ch[j]=2
    return primes

if __name__ == "__main__":
    n = int(input())
    primes = find_prime_nums(n)
    length = len(primes)
    rt = 0
    cnt = 0
    sum_ = 0
    for lt in range(length):
        while sum_<n and rt<length:
            sum_ += primes[rt]
            rt += 1
        if sum_ == n:
            cnt += 1
        sum_ -= primes[lt]
    print(cnt)
       