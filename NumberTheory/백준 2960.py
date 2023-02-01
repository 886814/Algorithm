def Eratosthenes(n,k):
    cnt = 0
    ch=[0]*(n+1)
    for i in range(2, n+1):
        if ch[i]==0:
            cnt += 1
            ch[i] = 1
            if cnt == k:
                print(i)
            for j in range(i+i, n+1, i):
                if ch[j] != 1:
                    ch[j] = 1
                    cnt += 1
                    if cnt == k:
                        print(j)

if __name__ == "__main__":
    n,k = map(int,input().split())
    Eratosthenes(n,k)
