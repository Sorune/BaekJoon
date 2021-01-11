n=input().split(" ")
N = int(n[0])
X = int(n[1])
A=[]
AN=input().split(" ")
for i in AN:
    o=int(i)
    A.append(o)
for i in A:
    if i<X:
        print(i)
    else:
        pass
