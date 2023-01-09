min_,max_ = map(int,input().split())
ch=[1]*(max_-min_+1)
i = 2
while i*i <= max_:
    temp = min_ // i**2
    while temp*(i**2) <=max_:
        if 0 <= temp*(i**2)-min_ <= max_-min_:
            ch[temp*(i**2)-min_] = 0
        temp += 1
    i += 1
print(sum(ch))
