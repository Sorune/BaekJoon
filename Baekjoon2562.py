import sys
N=[0 for i in range(9)]
for i in range(9):
    N[i]=int(input())
print(max(N))
print(N.index(max(N))+1)