def solution(word):
    return sum(["AEIOU".index(n) *(5**(5-i)-1) / 4 + 1 for i, n in enumerate(word)])