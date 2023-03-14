import sys

def check(num):
    for i in range(1,len(num)//2+1):
        if num[-2*i:-i] == num[-i:]:
            return False
    return True

def DFS(num, k):
    if k == n:
        print(num)
        sys.exit()
    else:
        for s in nums:
            if check(num+s):
                DFS(num+s, k+1)
        
n = int(input())
nums = '123'
for num in nums:
    DFS(num, 1)