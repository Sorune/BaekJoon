import sys
A=int(sys.stdin.readline().rstrip())
for i in range(A):
    N=sys.stdin.readline().rstrip()
    N=N.split(" ")
    print(int(N[0])+int(N[1]))