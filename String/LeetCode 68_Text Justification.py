from itertools import zip_longest
words = ["This", "is", "an", "example", "of", "text", "justification."]
#words = ["What","must","be","acknowledgment","shall","be"]
#words = ["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"]
maxWidth = 16
tmp = []
res = []
ans = []

for word in words:
    tmp.append(word)
    if len("".join(tmp)) + len(tmp) - 1 > maxWidth:
        tmp_word = tmp.pop()
        res.append(tmp)
        tmp = [tmp_word]
        
for s in res:
    # 공백추가
    if len(s) > 1:
        blank = maxWidth - len("".join(s))
        n_blank = blank // (len(s)-1)
        mod = blank % (len(s)-1)
        mod_blank = [" " for _ in range(mod)]
        b = " "*n_blank
        if mod > 0:
            result = ""
            for x,y in zip_longest(s, mod_blank, fillvalue=""):
                result += x + b + y
            ans.append(result.strip())
        else:
            ans.append(b.join(s))
    else:
        # 단어 한개면
        ans.append(s[-1].ljust(maxWidth," "))
else:
    # 마지막 줄
    if len(tmp) > 1:
        string = " ".join(tmp)
        ans.append(string.ljust(maxWidth," "))
    else:
        ans.append(tmp[-1].ljust(maxWidth," "))
    
for answer in ans:
    print(answer)