Chr=[]
for c in range(97,123):
    Chr.append(chr(c))
a=input()
for i in Chr:
    if i in a:
        locate=a.find(i)
        print(locate,end=' ')
    elif i not in a:
        print(-1,end=' ')