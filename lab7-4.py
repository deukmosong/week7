import math
for i in range(2,11):
    print('4**',i,'=',4**i)

    #################### 7-4 2번문제
for i in range(0,181,10):
    a=math.radians(i)
    print('{}degrree={:.3f}radian'.format(i,a))

       #################### 7-4 3번문제
for i in range(0,181,10):
    a=math.sin(math.radians(i))
    print('sin({})={:.2f}'.format(i,a))