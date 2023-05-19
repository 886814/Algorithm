import sys
S = input()
T = input()

def DFS(S, T):
    if S == T:
        print(1)
        sys.exit(0)
    else:
        if T and T[-1] == 'A':
            DFS(S, T[:-1])
        if T and T[0] == 'B':
            DFS(S, T[1:][::-1])
            
DFS(S,T)
print(0)