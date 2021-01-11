N=[0 for i in range(10)]
R=N
c=0
for i in range(0,len(N)):
    N[i]=int(input())   
for i in range(len(R)):
    R[i]=N[i]%42
for i in R:
    for l in range(0,1001):
        if R.count(l)>0:    
            c+=1                
        else:
            pass
print(c)
