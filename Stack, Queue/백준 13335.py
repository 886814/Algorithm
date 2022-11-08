n,bridge_length,weight = map(int,input().split())
truck_weights = list(map(int,input().split()))
q=[0]*bridge_length
sec=0
sum_q = sum(q)
while q:
    sec+=1
    sum_q -= q.pop(0)
    if truck_weights:
        if sum_q+truck_weights[0]<=weight:
            temp = truck_weights.pop(0)
            q.append(temp)
            sum_q+=temp
        else:
            q.append(0)
print(sec)