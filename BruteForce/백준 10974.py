import itertools as it
n = int(input())
for x in it.permutations(range(1,n+1),n):
    print(*x)