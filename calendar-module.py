#  problem link = https://www.hackerrank.com/challenges/calendar-module/problem
# the input is first converted to int and then added to list
# strftime means string from time . we can format the time in different desirable ways.
# format specifier %A is used for full day name
# more info at https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes

import datetime as dt
date_input = input()
date_list = list(map(int, date_input.split()))
year = date_list[2]
month = date_list[0]
date = date_list[1]
d = dt.date(year, month, date)
day = d.strftime("%A")
print(day.upper())
