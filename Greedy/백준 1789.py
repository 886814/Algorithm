# s = int(input())
# for i in range(1,s+1):
#     if i*(i+1)//2 <= s and s < (i+1)*(i+2)//2:
#         print(i)

s = int(input())
num = int((-1 + (1+8*s)**0.5)//2)
print(num)