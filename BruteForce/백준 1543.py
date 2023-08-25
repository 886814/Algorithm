string = input()
word = input()
index, cnt = 0, 0
while index + len(word) <= len(string):
    if not string[index:index+len(word)] == word:
        index += 1
    else:
        cnt += 1
        index += len(word)
print(cnt)