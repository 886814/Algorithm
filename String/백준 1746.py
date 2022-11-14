n,m = map(int,input().split())
ans, dic = [], {}
for _ in range(n+m):
    name = input()
    dic[name] = dic.get(name,0)+1
for name, cnt in dic.items():
    if cnt == 2:
        ans.append(name)
ans.sort()
print(len(ans))
for a in ans:
    print(a)