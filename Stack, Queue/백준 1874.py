import sys
input = sys.stdin.readline
n = int(input())
stack = []
ans = []
tmp = 1
for i in range(n):
    pop = int(input())
    while tmp <= pop:
        stack.append(tmp)
        ans.append('+')
        tmp += 1
    if stack.pop() == pop:
        ans.append('-')
    else:
        print('NO')
        break
else:
    print('\n'.join(ans))