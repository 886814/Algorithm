n = int(input())
arr = list(map(int,input().split()))
m = int(input())
arr.sort()
left, right = 0, n - 1
ans = 0

while left < right:
    tmp = arr[left] + arr[right]
    if tmp == m:
        ans += 1
    if tmp < m:
        left += 1
        continue
    right -= 1
print(ans)