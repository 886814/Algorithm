import math
from fractions import Fraction
n,m = map(int,input().split())
print(Fraction(math.factorial(n),math.factorial(m)*math.factorial(n-m)))
