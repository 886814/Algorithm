import itertools as it
from functools import reduce
operators = ["+","-"," "]
t = int(input())
for _ in range(t):
    answers = []
    n = int(input())
    a = list(map(str,range(1,n+1)))
    for i in it.product(operators,repeat = n-1):
        temp = reduce(lambda x,y : x+y,[(x,y) for x,y in zip(a[:-1],i)])
        string = "".join(temp)+a[-1]
        if eval(string.replace(" ","")) == 0:
            answers.append(string)
    answers.sort()
    for answer in answers:
        print(answer)
    print()