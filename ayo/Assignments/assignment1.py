import datetime

time_now = datetime.datetime.now()

formatted_line = time_now.strftime("%A. %B,%d %Y. %Ipm")
print(formatted_line)