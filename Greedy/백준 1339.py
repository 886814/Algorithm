from collections import defaultdict
n=int(input())
alphabet = defaultdict(int)
for i in range(n):
    txt = input()
    for j in range(len(txt)):
        alphabet[txt[j]] += 10 ** (len(txt) - j - 1)

nums = sum([(9-i)*x for i,x in enumerate(sorted(list(alphabet.values()), reverse=True))])

print(nums)
