import datetime


time_now = datetime.datetime.now()

print(time_now)

formatted_time = time_now.strftime("%A %b, %Y.  (%I%p)")
print(formatted_time)