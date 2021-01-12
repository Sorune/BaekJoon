a=input()
a=a.lower()
a=list(a)
b=list(set(a))
c=[]
for i in b:
    c.append(a.count(i))
d=max(c)
e=c.count(d)
f=c.index(d)
if e>1:
    print('?')
elif e==1:
    
    print(b[f].upper())