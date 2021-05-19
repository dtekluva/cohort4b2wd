
import datetime

date_time = datetime.datetime.now()

date_of_birth = input('Please enter your date of Birth: ')
convert = int(date_of_birth.split()[0]) 
soln = date_time.year - convert

print(f'{date_of_birth.split()[0]} - {date_of_birth.split()[1]} - {date_of_birth.split()[2]}')


