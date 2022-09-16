def hong(s,m):
    global n
    m += 1
    if len(s) == 2*n-1:
        temp = s.replace(" ","")
        if eval(temp) == 0:   
            print(s)
            return
    else:
        hong(s+" "+str(m),m)
        hong(s+"+"+str(m),m)
        hong(s+"-"+str(m),m)

t = int(input())
for _ in range(t):
    n = int(input())
    hong("1",1)
    print()