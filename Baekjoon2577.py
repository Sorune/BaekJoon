N=[0 for i in range(3)]
for i in range(3):
    N[i]=int(input())
result = str(N[0]*N[1]*N[2])
for i in range(0,10):
    print(result.count(str(i)))