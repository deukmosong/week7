def sum1to1000000():
    sum=0
    for i in range(1000001):
        sum+=i
    return sum
    
def fact1000():
    sum=1
    for i in range(1001):
        sum*=i
    return sum
def iii():
    sum=0
    for i in range(1,1000,2):
        sum=sum+(i*i*i)
        print(sum)
    return sum
import time
beforetime=time.time()
for i in range(100):
    sum1to1000000()
print('1에서 1000000까지의 합을 100번 반복해서 구하는 시간:{:.4f}'.format(time.time()-beforetime))
beforetime=time.time()
for i in range(100):
    fact1000()
print('1000!을 100번 반복해서 구하는 시간:{:.4f}'.format(time.time()-beforetime))
answer=iii()
print('1에서 1000까지의 홀수의 세제곱 더하기 결과:',answer)
beforetime=time.time()
'''for i in range(100):
    iii()
print('1에서 1000까지의 홀수의 세제곱 100번 하는시간:{:.4f}'.format(time.time()-beforetime))'''
