C = int(input())
for i in range(1,C+1):
    N = input()
    N = N.split(' ')
    A = int(N[0])
    B = int(N[1])
    print("Case #{}:".format(i),A,"+",B,"=",A+B)