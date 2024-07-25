n = int(input())
lt,rt = 0,n
while lt < rt:
    mid = (lt + rt) // 2
    if mid*mid >= n:
        rt = mid
    else:
        lt = mid + 1
print(lt)