import datetime
import os
from datetime import date
import calendar
import datetime
sn = 0
days = datetime.datetime.today().day
months = datetime.datetime.today().month
my_date = date.today() - datetime.timedelta(days=0)
dw = calendar.day_name[my_date.weekday()]
f = open('ff.css', 'w')
f.write('<!DOCTYPE html>')
f.write('\n</tr>')
f.closed
