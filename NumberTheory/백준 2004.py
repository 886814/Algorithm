n,m=map(int,input().split())

def factorial_5or2_cnt(num,t):
  cnt=0
  while num>0:
    cnt+=num//t
    num//=t
  return cnt

cnt_5=factorial_5or2_cnt(n,5)-factorial_5or2_cnt(m,5)-factorial_5or2_cnt(n-m,5)
cnt_2=factorial_5or2_cnt(n,2)-factorial_5or2_cnt(m,2)-factorial_5or2_cnt(n-m,2)
result=min(cnt_5,cnt_2)
print(result)
