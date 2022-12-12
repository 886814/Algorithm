import math
a,b = map(int,input().split())
c,d = map(int,input().split())

gcd = math.gcd((a*d + c*b),b*d)
numerator = (a*d + c*b)//gcd
denominator = (b*d)//gcd

print(numerator, denominator)