survey = ["TR", "RT", "TR"]
choices = [7,1,3]
dic = {"R":0,"T":0,"C":0,"F":0,"J":0,"M":0,"A":0,"N":0}
a = [("R","T"),("C","F"),("J","M"),("A","N")]
ans = ""

for s,c in zip(survey,choices):
    l,r = s[0],s[1]
    if c >= 5:
        dic[r] += c-4
    elif c <= 3:
        dic[l] += 4-c

for i in a:
    x,y = i
    if dic[x] >= dic[y]:
        ans += x
    else :
        ans += y
        
print(ans)