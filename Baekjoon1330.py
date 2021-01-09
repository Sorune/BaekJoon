Num=input()
Num=Num.split(' ')
a=int(Num[0])
b=int(Num[1])
if a<b:
    print("<")
elif a>b:
    print(">")
elif a == b:
    print("==")