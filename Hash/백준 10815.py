n = int(input())
a = list(map(int,input().split()))
dic = {}
for i in a:
    dic[i] = '1'
m = int(input())
b = list(map(int,input().split()))

print(' '.join(dic.get(m,'0') for m in b))