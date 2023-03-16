import math
n = int(input())
trees = [int(input()) for _ in range(n)]
gcd = math.gcd(*[trees[j+1] - trees[j] for j in range(len(trees)-1)])
print((trees[-1] - trees[0]) // gcd - n + 1)
