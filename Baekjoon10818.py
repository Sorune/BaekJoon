N=int(input())
A=input().split(" ")
B=[0 for i in range(N)]
for i in range(N):
    B[i]=int(A[i])
print(min(B),max(B))
