import math
t = int(input())
ch=[True]*(2000001)
q = []
for i in range(2, int(math.sqrt(2000001))+1):
    if ch[i]:
        for j in range(i+i, 2000001, i):
            if ch[j]:
                ch[j] = False

for i in range(2,2000001):
    if ch[i]:
        q.append(i)

def is_prime(x):
    for i in q:
        if i*i > n-2:
            break
        if (n-2) % i == 0: 
            return 0
    return 1

for _ in range(t):
    n = sum(map(int,input().split()))
    if n < 4:
        print("NO")
    elif n % 2  == 0:
        print("YES")
    else:
        if is_prime(n-2):
            print("YES")
        else:
            print("NO")
            