# G = int(input())
# P = int(input())
G,P = 4,6
gates = [-1]*(G+1)
cnt = 0
for i in range(1,P+1):
    gate = int(input())
    if gates[gate] == -1:
        gates[gate] = gate-1
        cnt += 1
    else:
        for j in range(gates[gate],0,-1):
            if gates[j] == -1:
                gates[j] = j-1
                gates[gate] = gates[j]
                cnt += 1
                break
        else:
            break
print(cnt)