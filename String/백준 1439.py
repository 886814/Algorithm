s = input()
now_ = s[0]
dic = {'0':0, '1':0}
for i in s:
    if i != now_:
        dic[now_] += 1
        now_ = i
else:
    dic[now_] += 1

print(min(dic.values()))