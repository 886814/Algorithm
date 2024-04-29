from math import gcd
def getGCD(arr):
    gcd_ = arr[0]
    for num in arr:
        gcd_ = gcd(num,gcd_)
    return gcd_

def check(arr, gcd):
    for num in arr:
        if num % gcd == 0:
            return 0
    return gcd

arrayA = [14,35,119]
arrayB = [18,30,102]

gcdA = getGCD(arrayA)
gcdB = getGCD(arrayB)

print(max(check(arrayB, gcdA), check(arrayA, gcdB)))