N=input()
C=[0,0]
C[0],C[1]=N[0],N[1]
n=int(N)
c=0
A=[0,0]
B=[0,0]
while True:
   
    while True:
        c+=1
        if n < 10:
            A[0]=0
            A[1]=int(C[1])
        else:
            A[0]=int(C[0])
            A[1]=int(C[1])
            B[0]=A[1]
            if (A[0]+A[1])>=10:
                s=str(A[0]+A[1])
                B[1]=int(s[1])
                C[0]=str(B[0])
                C[1]=str(B[1])
                continue
            else:
                B[1]=A[0]+A[1]
                if (str(B[0])+str(B[1]))==N:
                    print(c)
                    break
                else:
                    n=int(str(B[0])+str(B[1]))
                    C[0]=str(B[0])
                    C[1]=str(B[1])
                    continue
    break