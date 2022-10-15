import random as r

romio_num=r.randrange(1,7)
juliet_num=r.randrange(1,7)
print('로미오의 주사위 수는',romio_num,'입니다')
print('줄리엣의 주사위 수는',juliet_num,'입니다')

if romio_num==juliet_num:
    print("로미와 줄리엣이 비겼습니다")
elif romio_num>juliet_num:
    print('로미오가 이겼습니다')
else :
    print('줄리엣이 이겼습니다')
