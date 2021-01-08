Num = int(input())
End = Num*2-1
le, ri = Num-1,-1
for i in range(Num):
    if i == 0:
        Sp = Num-1
        print(' '*Sp+'*')
        pass
    elif 0<i<Num-1 :
        le -=1 
        ri += 2
        Left=' '*le+'*'
        Right=' '*ri+'*'
        result = Left+Right
        print(result)
        pass
    elif i==Num-1:
        print('*'*End)