from itertools import permutations

def check(nums,k):
    now = k
    for num in nums:
        min_piro, consume_piro = num
        if now >= min_piro:
            now -= consume_piro
        else:
            return 0
    else:
        return 1

def solution(k, dungeons):

    for i in range(len(dungeons),-1,-1):
        for x in permutations(dungeons,i):
            if check(x,k):
                return i