import datetime
x = datetime.datetime.now()
print(x)
date = datetime.date.today()
print(date)
str_date = x.strftime("%D")
print(str_date)
str_time = x.strftime("%H:%M:%S")
print(str_time)
str_day = x.strftime("Today is %d %B,%Y and the day is %A")
print(str_day)
