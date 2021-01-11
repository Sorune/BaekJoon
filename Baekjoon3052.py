N=[0 for i in range(10)]
R=N
C=[]
for i in range(0,len(N)):
    N[i]=int(input())   
for i in range(len(R)):
    R[i]=(N[i]%42)
for i in R:
    if i not in C:
        C.append(i)
print(len(C))
