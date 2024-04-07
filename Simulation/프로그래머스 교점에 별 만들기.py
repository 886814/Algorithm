from itertools import combinations

def intersection_point(l1,l2):
    A, B, E = l1
    C, D, F = l2

    if A*D == C*B:
        return

    x = (B*F-E*D)/(A*D-B*C)
    y = (E*C-A*F)/(A*D-B*C)

    if x == int(x) and y == int(y):
        return (int(x),int(y))

def solution(line):
    stars = []
    for l1,l2 in combinations(line,2):
        point = intersection_point(l1,l2)
        if point:
            stars.append(intersection_point(l1,l2))

    x1, x2 = sorted(stars, key=lambda x : x[0])[0][0], sorted(stars, key=lambda x : -x[0])[0][0] + 1
    y1, y2 = sorted(stars, key=lambda x : x[1])[0][1], sorted(stars, key=lambda x : -x[1])[0][1] + 1

    gezi = [["."] * (x2-x1) for _ in range(y2-y1)]

    for x,y in stars:
        gezi[y-y1][x-x1] = "*" 

    gezi.reverse()
    return [''.join(a) for a in gezi]