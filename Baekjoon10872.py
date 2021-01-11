def sdd(a):
    if a ==0:
        return 1
    else:
        return a * sdd(a-1)

N=int(input())
result = sdd(N)
print(result)