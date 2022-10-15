import datetime as d
today=d.datetime.now()
print('오늘은 {}년 {}월 {}일입니다'.format(today.year,today.month,today.day))
firstdate=d.datetime(2019,2,24)
print('춘향이와 몽룡이의 연얘시작일 : {}년 {}월 {}일'.format(firstdate.year,firstdate.month,firstdate.day))
print('연애시작일로 부터 경과한 날짜',(today-firstdate).days)
day100=d.timedelta(days=100)
day200=d.timedelta(days=200)
day500=d.timedelta(days=500)
day1000=d.timedelta(days=1000)
print('100일 기념일:',firstdate+day100)
print('200일 기념일:',firstdate+day200)
print('500일 기념일:',firstdate+day500)
print('1000일 기념일:',firstdate+day1000)


