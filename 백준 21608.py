import sys
input = sys.stdin.readline
n = int(input())
map_ = dict()
for i in range(1, n*n+1):
    student, *like = map(int,input().split())
    map_[student] = like
a = [[0] * n for _ in range(n)]
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def condition1(student,like):
    coordinate = []
    tmp = dict()
    max_ = 0
    for x in range(n):
        for y in range(n):
            count = 0
            if a[x][y] != 0:
                continue
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < n:
                    if a[nx][ny] in like:
                        count += 1
                        max_ = max(max_, count)
            tmp[(x,y)] = count
    for key, value in tmp.items():
        if value == max_:
            coordinate.append((student,key))
    return coordinate

def condition2(coordinates):
    candidate = []
    tmp2 = dict()
    max_ = 0
    for student,value in coordinates:
        count = 0
        x,y = value
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n:
                if a[nx][ny] == 0:
                    count += 1
                    max_ = max(max_, count)
        tmp2[(student,(x,y))] = count
    for key, value in tmp2.items():
        if value == max_:
            candidate.append((key))
    return candidate

for student, like  in map_.items():
    student_no = condition1(student,like)
    if len(student_no) > 0:
        student_no = condition2(student_no)
    student_no = sorted(student_no, key=lambda x: (x[0], x[1]))[0]
    no_,x,y = student_no[0], student_no[1][0], student_no[1][1]
    a[x][y] = no_

satisfactions = dict()
for x in range(n):
    for y in range(n):
        cnt = 0
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n:
                if a[nx][ny] in map_[a[x][y]]:
                    cnt += 1
        satisfactions[a[x][y]] = int(10**(cnt-1))
print(sum([value for value in satisfactions.values()]))