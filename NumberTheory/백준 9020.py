if __name__ == "__main__":
    t = int(input())
    ch=[True]*(1000001)
    for i in range(2, 1001):
        if ch[i]:
            for j in range(i+i, 1000001, i):
                if ch[j]:
                    ch[j] = False
    for _ in range(t):
        n = int(input())
        A = n // 2
        B = A
        for _ in range(10000):
            if ch[A] and ch[B]:
                print(A, B)
                break
            A -= 1
            B += 1
