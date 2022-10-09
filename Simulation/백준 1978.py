import math
def is_prime_number(x):
    if x == 1:
        return False
    for i in range(2, int(math.sqrt(x))+1):
        if x % i == 0:
            return False
    return True

n = int(input())
numbers = list(map(int,input().split()))
cnt = 0
for number in numbers:
    if is_prime_number(number):
        cnt += 1
print(cnt)