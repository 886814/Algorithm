import sys
input = sys.stdin.readline
n,m = map(int,input().split())
bundle, single = 1001, 1001
for i in range(m):
    x,y = map(int,input().split())
    bundle = min(bundle,x)
    single = min(single,y)

tmp1 = (n//6+1)*bundle
tmp2 = n*single
res = (n//6)*bundle + (n%6)*single
res = min(min(res,tmp1),tmp2)
print(res)