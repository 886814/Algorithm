import sys
if __name__ == "__main__":
    ch=[True]*(1000001)
    for i in range(2, 1001):
        if ch[i]:
            for j in range(i+i, 1000001, i):
                if ch[j]:
                    ch[j] = False
    while True:
        n = int(sys.stdin.readline())
        if n == 0:
            break
        for i in range(3,n):
            if ch[i] and ch[n-i]:
                print(f"{n} = {i} + {n-i}")
                break
