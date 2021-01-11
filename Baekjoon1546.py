N=int(input())
C=[0 for i in range(N)]
Score = input().split(" ")
for i in range(N):
    Score[i]=int(Score[i])
Max = max(Score)
result = [0 for i in range(N)]
replace = 0
for i in range(N):
    result[i] = (Score[i]/Max)*100
for i in range(N):
    replace+=result[i]
replace = replace/N
print(replace)
