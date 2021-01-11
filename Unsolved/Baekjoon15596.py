def solve(a: list):
    n = int(input())
    result = 0
    a=[0 for i in range(n)]
    for i in range(n):
        a[i]=int(input())
    for i in range(n):
        result+=a[i]
    return print(result)


solve(1)