def aver(a):
    for i in range(a):
        A=input().split(" ")
        Stu=[float(0)]*int(A[0])
        n=float(0) 
        answer=float(0)
        for l in range(1,len(A)):
            answer+=int(A[l])
        n=answer/int(A[0])
        for p in range(1,len(Stu)+1):
            if float(A[p])>n:
                Stu[p-1]='pass'
            else: Stu[p-1]='unpass'
        n=round((Stu.count('pass')/int(A[0]))*100,3)
        print('%0.3f'%n +"%")

a=int(input())
aver(a)