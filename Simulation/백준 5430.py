from collections import deque
t = int(input())
for _ in range(t):
    p = input()
    n = int(input())
    temp = input()[1:-1]
    a = temp.split(',') if len(temp)> 0 else []
    a = deque(a)
    cnt = 0
    for i in p:
        if i == 'R':
            cnt += 1
        elif i == 'D':
            if len(a) == 0:
                print('error')
                break
            else:
                if cnt % 2 == 0:
                    a.popleft()
                else:
                    a.pop()
    else:
        if cnt % 2 == 1:
            a.reverse()
        print('['+",".join(a)+']')