n = int(input())
friends = [list(input()) for _ in range(n)]
isfriend = [[0] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        for k in range(n):
            if i == j:
                continue
            if friends[i][j] == "Y" or (friends[i][k] == "Y" and friends[k][j] == "Y"):
                isfriend[i][j] = 1

print(max([sum(x) for x in isfriend]))
