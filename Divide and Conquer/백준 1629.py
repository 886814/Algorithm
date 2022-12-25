import sys
a,b,c = map(int,sys.stdin.readline().split())

def DivideNConquer (a,n):
  if n == 1:
      return a%c
  else:
      tmp = DivideNConquer(a,n//2)
      if n %2 ==0:
          return (tmp * tmp) % c
      else:
          return (tmp  * tmp *a) %c
          
print(DivideNConquer(a,b))

# 별해
import sys
a,b,c = map(int,sys.stdin.readline().split())
print(pow(a,b,c))
