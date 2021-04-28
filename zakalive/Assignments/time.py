import datetime

time_now = datetime.datetime.now()
day = time_now.day
month = time_now.month

formatted_time = time_now.strftime("%a. the - %d/%m/%y, %H:%M:%S")
print(formatted_time)
