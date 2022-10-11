import itertools as it
l,c = map(int,input().split())
letters = input().split()
temp = ['a','e','i','o','u']
ans = []
vowels = [letter for letter in letters if letter in temp]
letters = [letter for letter in letters if letter not in temp]
for i in range(1, len(vowels)+1):
    for x in it.combinations(vowels,i):
        for y in it.combinations(letters,l-i):
            if len(y) < 2:
                continue
            ans.append("".join(sorted(x+y)))
for a in sorted(ans):
    print(a)