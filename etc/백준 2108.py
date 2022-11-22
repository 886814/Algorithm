from collections import Counter
import sys
input = sys.stdin.readline
n = int(input())
nums = []
for i in range(n):
    nums.append(int(input()))
print(round(sum(nums)/n))
print(sorted(nums)[n//2])
most = Counter(nums).most_common(n)
temp = [most[i] for i in range(len(most)) if most[i][1] == most[0][1]]
temp.sort(key = lambda x: x[0])
print(temp[1][0]) if len(temp) > 1 else print(temp[0][0])
print(max(nums)-min(nums))