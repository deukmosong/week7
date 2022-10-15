import datetime as d
today=d.datetime.now()
print('오늘은 {}년 {}월 {}일입니다'.format(today.year,today.month,today.day))
xmas=d.datetime(2025,12,25)
dayleft=xmas-today.now()
print('2025년 크리스마스 까지는 {}일 {}시간 남았습니다'.format(dayleft.days,dayleft.seconds//3600))
###########################7-2번 문제
print('오늘은 {}년 {}월 {}일입니다'.format(today.year,today.month,today.day))
newyear=d.datetime(2036,1,1)
dayleft=newyear-today
print('2036년 새해 까지는 {}일 {}시간 남았습니다'.format(dayleft.days,dayleft.seconds//3600))
