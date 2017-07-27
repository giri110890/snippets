'''
from datetime import datetime, timedelta

s = '01.07.2017 23:45'
date = datetime.strptime(s, "%d.%m.%Y %H:%M")
for i in range(96):
    date = date + timedelta(minutes=15)
    final = datetime.strftime(date, "%d.%m.%Y %H:%M")
    print((final))
'''
print(2**16)
print(3**2)
