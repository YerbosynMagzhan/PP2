from datetime import datetime, timedelta
currdate = datetime.now()
zavtra = currdate + timedelta(days = 1)

diff = (currdate - zavtra).total_seconds()
print(diff)