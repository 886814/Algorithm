from collections import Counter
import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    clothes = []
    n = int(input())
    for _ in range(n):
        _, body = input().split()
        clothes.append(body)
    clothes_count = Counter(clothes)
    ans = 1
    for num in clothes_count.values():
        ans *= num + 1
    print(ans-1)