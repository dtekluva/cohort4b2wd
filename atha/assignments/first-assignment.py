import datetime

time_now = datetime.datetime.now()
day = time_now.day
month = time_now.month


 print(time_now)
 print(day)
 print(month)

 special formatting

formatted_time = time_now.strftime("%a. The - %m/%d/%Y, %H:%M:%S")
print(formatted_time) 

new_format_time = time_now.strftime("%A. %b, %Y. (%I%p)")
print(new_format_time)