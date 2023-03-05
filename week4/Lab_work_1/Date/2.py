import datetime as d

currdate = d.date.today()
zavtra = currdate + d.timedelta(days=1)
vchera = currdate - d.timedelta(days = 1)
print('yesterday', vchera)
print('today',currdate)
print('tomorrow',zavtra)