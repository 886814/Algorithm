def calc(count):
    return 6 if count < 2 else 7 - count

def solution(lottos, win_nums):
    cnt, zero = 0, 0
    for lotto in lottos:
        if lotto == 0:
            zero += 1
        elif lotto != 0 and lotto in win_nums:
            cnt += 1 

    return [calc(cnt+zero), calc(cnt)]