import itertools as it
users = [[40,10000],[25,10000]]
emoticons = [7000,9000]
discount = [10,20,30,40]
dis_per = [x for x in it.product(discount,repeat = len(emoticons))]
ans = 0
a = []
for dis in dis_per:
    temp = list(zip(dis,emoticons))
    plus = 0
    res = 0
    for user in users:
        tot = 0
        ratio, price = user
        for tmp in temp:
            if tmp[0] >= ratio:
                tot += tmp[1] * (100-tmp[0])/100
        if tot >= price:
            plus += 1
        else:
            res += tot
    a.append((plus, res))
a.sort(key=lambda x : (-x[0],-x[1]))