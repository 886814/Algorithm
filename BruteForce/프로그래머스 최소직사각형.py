def solution(sizes):
    max_, min_ = 0, 0
    for x,y in sizes:
        if x > y:
            max_ = max(max_,y)
            min_ = max(min_,x)
        else:
            max_ = max(max_,x)
            min_ = max(min_,y)
    return max_ * min_