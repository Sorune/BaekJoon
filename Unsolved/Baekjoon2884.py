Hour=input()
Hour=Hour.split(' ')
H = int(Hour[0])
M = int(Hour[1])
M-=45
if M<0:
    H-=1
    M+=60
    if H<0:
        H+=24
        print(H,M)
    elif H>24:
        H=H-24
        H=abs(H)
        print(H,M)
    elif 0<H<24:
        print(H,M)
elif M>60:
    H+=1
    M-=60
    if H<0:
        H+=24
        print(H,M)
    elif H>24:
        H=H-24
        H=abs(H)
        print(H,M)
    elif 0<H<24:
        print(H,M)
else :
    print(H, M)