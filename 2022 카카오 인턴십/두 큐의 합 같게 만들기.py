from collections import deque
queue1 = [1,1]
queue2 = [1,5]
q1,q2 = deque(queue1), deque(queue2)
sum1,sum2 = sum(queue1), sum(queue2)
max_cnt = len(queue1) * 3
cnt = 0
while (q1 and q2) and max_cnt >= cnt:
    if sum1 == sum2:
        print(cnt)
        break
    else:
        if sum1 > sum2:
            temp = q1.popleft()
            q2.append(temp)
            sum1 -= temp
            sum2 += temp
            cnt += 1
        else:
            temp = q2.popleft()
            q1.append(temp)
            sum2 -= temp
            sum1 += temp
            cnt += 1
else:
    print(-1)        
