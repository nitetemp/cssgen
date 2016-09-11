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
f.write('\n<html>')
f.write('\n<head>')
f.write('\n<style>')
f.write('\ntable, th, td {')
f.write('\n    border: 2px solid black;')
f.write('\n}')
f.write('\n</style>')
f.write('\n<body>')
f.write('\n<>')
f.write('\n<table style="width:100%">')
f.write('\n<tr>')
f.write('\n<th>S.No</th>')
f.write('\n<th>Name of Product</th>')
f.write('\n<th>Picture of Product</th>')
f.write('\n<th>Quality of Product</th>')
f.write('\n</tr>')
f.write('\n</table>')
f.write('\n</body>')
f.write('\n</head>')
f.write('\n</html>')
f.closed
