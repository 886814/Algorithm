x,y,w,s = map(int,input().split())
diag, stra = min(x,y), abs(x-y)
ans = diag * min(s,2*w) + 2 * (stra // 2) * min(s,w) + (stra % 2) * w
print(ans)