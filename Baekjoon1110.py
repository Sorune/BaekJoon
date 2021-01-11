# 주어지는 수는 무조건 2자리로 받을 것/2열 리스트
# 주어진 수를 2자리로 구분, 이전의 일의 자리 숫자를 십의 자리로, 십의 자리와 일의 자리를 더해서 일의 자리로해서
# 새로운 두 자리의 수를 구함
# 계속해서 반복하여 새로운 자리의 수가 처음 주어진 수와 같을 때 횟수 출력
N=input()
C=[0,0]
if int(N)<10:
    C[1]=int(N[0])
else:
    C[0],C[1]=int(N[0]),int(N[1])
n=int(N)
b=n
c=0
A=[0,0]
B=[0,0]
while True:
    while True:
        c+=1
        A[0]=C[0]
        A[1]=C[1]
        if b< 10:
            if (A[0]+A[1])>=10:
                s=str(A[0]+A[1])
                B[0]=A[1]
                B[1]=int(s[1])
                C[0]=B[0]
                C[1]=B[1]
                b=int(str(B[0])+str(B[1]))
                continue
            else:
                B[0]=A[1]
                B[1]=A[0]+A[1]
                if int(str(B[0])+str(B[1]))==n:
                    print(c)
                    break
                else:
                    b=int(str(B[0])+str(B[1]))
                    C[0]=B[0]
                    C[1]=B[1]
                    continue
        else:
            A[0]=int(C[0])
            A[1]=int(C[1])
            if (A[0]+A[1])>=10:
                s=str(A[0]+A[1])
                B[0]=A[1]
                B[1]=int(s[1])
                C[0]=B[0]
                C[1]=B[1]
                if int(str(B[0])+str(B[1]))==n:
                    print(c)
                    break
                else:
                    b=int(str(B[0])+str(B[1]))
                    C[0]=B[0]
                    C[1]=B[1]
                    continue
                b=int(str(B[0])+str(B[1]))
                continue
            else:
                B[0]=A[1]
                B[1]=A[0]+A[1]
                if int(str(B[0])+str(B[1]))==n:
                    print(c)
                    break
                else:
                    b=int(str(B[0])+str(B[1]))
                    C[0]=B[0]
                    C[1]=B[1]
                    continue
    break