a=int(input())
while True:
    result=a
    a=str(a)
    for i in range(len(str(a))):   
        result=result+int(a[i])
    a=result