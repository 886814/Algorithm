t = int(input())
for i in range(t):
    n,x,y = map(int,input().split())
    tmp = set(map(str,{x,y}))
    for num in range(n,0,-1):
        if set(str(num)) == tmp:
            print(f"#{i+1}", num)
            break
    else:
        print(f"#{i+1}", -1)