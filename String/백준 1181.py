import sys
n = int(input())
strings = set()
for i in range(n):
    strings.add(sys.stdin.readline().rstrip())
strings = sorted(strings,key=lambda x: (len(x),x))
for string in strings:
    print(string)