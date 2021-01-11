# 양의 정수 X의 각 자리수가 등차수열 ex)12 -> 1,2 1 차이

N=int(input())
c=0
n=[]
for i in range(1,N+1):
    n.append(i)
for i in range(N):
    s=str(n[i])
    if len(s)==1:
        c+=1
    elif len(s)==2:
        if abs((int(s[0])-int(s[1])))==abs((int(s[1])-int(s[0]))):
            c+=1
        else: pass
    elif len(s)==3:
        if abs((int(s[0])-int(s[1])))==abs((int(s[1])-int(s[2]))) and abs((int(s[1])-int(s[2]))==(int(s[0])-int(s[1]))):
            c+=1
        else: pass
print(c)