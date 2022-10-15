import random as rd
list=[]
for i in range(3):
    list.append(rd.randrange(0,100,5))
print(list)

###################7-5번 2번문제
list=[1,2,3,4,5,6,7,8,9,10]
list=rd.sample(list,3)
print(list)