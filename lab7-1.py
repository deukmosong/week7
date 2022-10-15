import datetime as dt
today=dt.datetime.now()
print('오늘의 날짜:{}년{}월{}일'.format(today.year,today.month,today.day))
if(today.hour>12):
    print('현재시간:오후{}시{}분{}초'.format(today.hour-12,today.minute,today.second))
else :
    print('현재시간:오전{}시{}분{}초'.format(today.hour,today.min,today.second))
