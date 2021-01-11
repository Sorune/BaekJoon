def num(a):
    result=a
    for i in list(str(a)):   
        result+=int(i)
    return result


n=range(1,10001)
number=[]
for i in n:
    number.append(num(i))

number.sort()
for i in n:
    if i in number:
        continue
    else: print(i)