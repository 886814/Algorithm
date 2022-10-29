import itertools as it
while True:
    inputs_ = list(map(int,input().split()))
    if inputs_[0] == 0:
        break
    k = inputs_[0]
    s = inputs_[1:]
    for i in it.combinations(s,6):
        print(*i)
    print()