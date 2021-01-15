from  datetime import date, timedelta
renew= date.today-timedelta(days=2).isoformat()
today=date.today()
print(renew)