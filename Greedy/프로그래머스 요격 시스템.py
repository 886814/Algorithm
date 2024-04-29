def solution(targets):
    answer = 1
    targets.sort(key = lambda x : x[1])
    temp = targets[0][1]
    for i in range(1, len(targets)):
        if temp <= targets[i][0]:
            temp = targets[i][1]
            answer += 1
    return answer