n = int(input())
inequalities = input().split()

def DFS(v, ch, s, type):
    global flag
    if flag:
        return
    if v == n+1:
        print(s)
        flag = True
    else:
        if type == 1:
            for j in range(9,-1,-1):
                if not ch[j] and (v == 0 or eval(s[-1] + inequalities[v-1] + str(j))):
                    ch[j] = True
                    DFS(v+1, ch , s + str(j), type)
                    ch[j] = False
        else:
            for j in range(10):
                if not ch[j] and (v == 0 or eval(s[-1] + inequalities[v-1] + str(j))):
                    ch[j] = True
                    DFS(v+1, ch , s + str(j), type)
                    ch[j] = False

ch = [False] * 10
flag = False
DFS(0,ch,"",1)
ch = [False] * 10
flag = False
DFS(0,ch,"",2)