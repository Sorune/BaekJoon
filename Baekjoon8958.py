def score(a):
    result=0
    score=0
    for i in range(a):
        insert=input()
        A=[0]*len(insert)
        for n in range(len(A)):
            if insert[n]=='O':
                score+=1
                A[n]=score
            else:
                score=0
        for i in range(len(A)):
            result+=A[i]
        print(result)
        result=0
        score=0

a=int(input())
score(a)