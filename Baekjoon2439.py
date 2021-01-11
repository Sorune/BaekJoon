N=int(input())
for i in range(1,N+1):
    Star='*'*i
    Blank=' '*(N-i)
    print(Blank+Star)
