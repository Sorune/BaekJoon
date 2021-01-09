# 자릿수 구하기
# 1번 숫자에 2번 숫자의 각 자리수만 곱하면 될 것
# 스트링 타입은 각 문자 단위로 자를 수 있음 따라서 스트링으로 받고 나눠받아서 정수로 캐스팅
# 그렇다면 ex) 472*385 = 472*5,472*8,472*3과 같이 구하고 마지막에 472*385
A=int(input())
B=input()
# B1=int(B[2])
# B2=int(B[1])
# B3=int(B[0])
# print(A*B1)
# print(A*B2)
# print(A*B3)
for i in range(2,-1,-1):
    print(A*int(B[i]))
print(A*int(B))