a=int(input())
result=str()
for i in range(a):
    C=input().split(" ")
    text=list(C[1])
    for l in range(len(text)):
        result+=(text[l]*int(C[0]))
        if (l+1)==len(text):
            print(result)
            result=str()

