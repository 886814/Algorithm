from collections import Counter
from functools import reduce

def sorting(A):
    B = []
    longest_row = 0
    # R연산
    for row in A:
        row = [x for x in row if x !=0] # 0 제거
        temp = sorted(Counter(row).items(),key = lambda x: (x[1],x[0])) # 문제에서 요구한 정렬
        temp = temp[:50] if len(temp) > 50 else temp # 최대 길이가 100이 넘어가면 100개이후는 컷
        longest_row = max(longest_row, len(temp)*2) # 최장길이 갱신
        B.append([y for x in temp for y in x]) # flatten 하기
    return [b + [0]*(longest_row - len(b)) for b in B] # 부족한 길이만큼 0 채우기

if __name__=="__main__":
    r,c,k = map(int,input().split())
    a = [list(map(int,input().split())) for _ in range(3)]
    
    for t in range(101):
        row_ = len(a)
        col_ = len(a[0])  
        try:
            if int(a[r-1][c-1]) == k:
                print(t)
                break
        except:
            pass
        # R 연산
        if row_ >= col_:
            a = sorting(a)
        # C 연산
        else:
            # transpose 하고 R 연산 후 다시 transpose
            a = list(map(list,zip(*sorting(list(map(list,zip(*a)))))))
    else:
        print(-1)