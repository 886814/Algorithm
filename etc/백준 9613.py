import sys
import math
n=int(input())

for i in range(n):
    arr=list(map(int, sys.stdin.readline().split()))
    sum_=0
    for j in range(1,len(arr)):
        for k in range(j+1,len(arr)):
            sum_+=math.gcd(arr[j],arr[k])

    print(sum_)