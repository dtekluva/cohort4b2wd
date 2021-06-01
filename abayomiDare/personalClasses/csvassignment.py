# import csv
# import datetime


# user_input = input('>> please enter key word > VAT: ')
# user_input = user_input.split(',')

# now = datetime.datetime.now()
# date_time = now.strftime("%Y-%m-%d %H:%M:%S")


# new_input = f'{user_input}_{date_time}.csv'
# print(new_input)


# file_path = r'/home/abayomidare/Desktop/Univelcity/cohort4b2wd/materials/gtb_doc.csv'

# f = open(file_path, 'w')

# top_column = ['Date', 'Debit', 'Credit', 'Remark'] 
    
# rows =  [[date_time, '0', '0', 'VAT']]

    
# # writing to csv file 
# with open(file_path, 'w') as csvfile: 
#     # creating a csv writer object 
#     csvwriter = csv.writer(csvfile) 
        
#     # writing to the top column
#     csvwriter.writerow(top_column) 
        
#     # writing the data rows 
#     csvwriter.writerows(rows)

#     f.close()