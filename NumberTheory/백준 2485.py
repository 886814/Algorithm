import math
n = int(input())
trees = []
tmp = 0
for i in range(n):
    x = int(input())
    trees.append(x)
gcd = math.gcd(*[trees[j+1] - trees[j] for j in range(len(trees)-1)])
print((trees[-1] - trees[0]) // gcd - n + 1)