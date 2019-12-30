import datetime
import time
import re

hello = datetime.datetime.now()

nowdate = hello.strftime('%Y-%m-%d %H:%M:%S')
print(nowdate)

test = ' 1시간 전 '
test2 = '1일 전'
numbers = re.findall('\d+', test)
print(numbers)

if '시간 전' in test:
    result = current - datetime.timedelta(hours=numbers)
    print('hour')
elif '달 전' in test:
    result = current - datetime.timedelta(month=numbers)
    print('month')
elif '일 전' in test:
    result = current - datetime.timedelta(days=numbers)
    print('day')
elif '분 전' in test:
    result = current - datetime.timedelta(minutes=numbers)
    print('minute')
elif '초 전' in test:
    result = current - datetime.timedelta(seconds=numbers)
    print('second')
else:
    print(error)



def qt_dae():
    hello = datetime.datetime.now()
    numbers = re.findall('\d+', test)
    print(numbers)

    for x in test:
        numbers = re.findall('\d+', test)

        if '시간 전' in test:
            result = current - datetime.timedelta(hours=numbers)
            print('hour')
        elif '달 전' in test:
            result = current - datetime.timedelta(month=numbers)
            print('month')
        elif '일 전' in test:
            result = current - datetime.timedelta(days=numbers)
            print('day')
        elif '분 전' in test:
            result = current - datetime.timedelta(minutes=numbers)
            print('minute')
        elif '초 전' in test:
            result = current - datetime.timedelta(seconds=numbers)
            print('second')
        else:
            print(error)

        result



