import datetime as d
today=d.datetime.now()
after=d.timedelta(days=1000)
print('오늘로 부터 1000일 후의 날짜는',today+after)
################## 2번문제
year,month,day=int(input('처음으로 사귄 연도와 월 일을 입력하시오:'))
first_date=d.datetime(year,month,day)
after=d.timedelta(days=100)
print('100일 기념일은 :',first_date+after)