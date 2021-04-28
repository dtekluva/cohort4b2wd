import datetime

time_now = datetime.datetime.now()
day = time_now.day
month = time_now.month

new_format_time = time_now.strftime("%A - %b,%d,%Y, (%I%p)")
print(new_format_time)
