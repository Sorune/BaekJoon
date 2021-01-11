A = input().split(" ")
low = int(A[0])
base = int(A[1])
price = int(A[2])
c=0
while True:
    c+=1
    if (low+(base*c)) <= price*c:
        print(c)
        break
    else :
        continue