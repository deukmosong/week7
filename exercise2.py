import random as r

rannum=r.randrange(1,21)
count=1

while(1):
    n=int(input('1~20까지의 수를 입력하세요'))
    if n>rannum:
        print(n,'보다  작습니다')
        count=count+1
    elif n<rannum:
        print(n,'보다 큽니다')
        count=count+1
    else :
        break
if count<=3:
    print(count,'번 만에 맞춘 당신은 천재')
elif count>=7:
    print(count,'번 만에 맞추다니 쩝쩝....')
else :
    print(count,'번 만에 맞추셧네요 잘했어요^^')
