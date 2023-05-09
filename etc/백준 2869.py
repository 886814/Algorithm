a,b,v = map(int,input().split())
if v < a:
    print(1)
if (v-a) % (b-a) == 0:
    print((v-a) // (a-b) +1)
else:
    print((v-a) // (a-b) +2)