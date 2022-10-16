from itertools import combinations_with_replacement as cwr
def solution(n, info):
    max_ = 0
    result = [-1]

    for x in cwr(range(11),n):
        ryan, apeach = 0, 0
        ryan_scores = [0 for _ in range(11)]
        for num in x:
            ryan_scores[10 - num] += 1
        for i in range(11):
            if ryan_scores[i] == 0 and info[i] == 0:
                continue
            elif ryan_scores[i] > info[i]:
                ryan += 10 - i
            else:
                apeach += 10 - i
        if max_ < ryan - apeach:
            max_ = ryan - apeach
            result = ryan_scores

    return result