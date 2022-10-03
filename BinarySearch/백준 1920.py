n = int(input())
a = list(map(int,input().split()))
a.sort()
m = int(input())
nums = list(map(int,input().split()))
for num in nums:
    lt,rt = 0, n-1
    while lt <= rt:
        mid = (lt+rt)//2
        if a[mid] == num:
            print(1)
            break
        elif a[mid] > num:
            rt = mid-1
        else:
            lt = mid+1
    else:
        print(0)