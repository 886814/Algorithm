n = int(input())
a = list(map(int,input().split()))
lis = [a[0]]
for num in a[1:]:
    if num > lis[-1]:
        lis.append(num)
    else:
        lt, rt = 0, len(lis)
        while lt < rt:
            mid = lt + (rt-lt)//2
            if lis[mid] < num:
                lt = mid + 1
            else:
                rt = mid
        else:
            lis[rt] = num
print(len(lis))

# 별해
from bisect import bisect_left
n = int(input())
a = list(map(int,input().split()))
lis = [a[0]]
for num in a[1:]:
    if num > lis[-1]:
        lis.append(num)
    else:
        lis[bisect_left(lis, num)] = num       
print(len(lis))
