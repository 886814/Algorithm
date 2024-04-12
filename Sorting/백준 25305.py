n, k = map(int,input().split())
scores = list(map(int,input().split()))
print(sorted(scores, reverse=True)[:k][-1])