import pymysql.cursors

# Connect to the database
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='',
                             database='school',
                             cursorclass=pymysql.cursors.DictCursor)

# table_name  = input("Please what table would you like to alter \n> ")
# column_name = input("Please what col name would you like to add \n> ")
# data_type   = input("Please enter datatype \n> ")
# qty   = input("Please input data-qty \n> ")


# with connection:
#     with connection.cursor() as cursor:
#         # Create a new record
#         sql = f"ALTER TABLE {table_name} ADD {column_name} {data_type}{f'({qty})' or qty}"
#         print(sql)
#         cursor.execute(sql)

#     # connection is not autocommit by default. So you must commit to save
#     # your changes.
#     connection.commit()


# table_name  = input("Please what table would you like to alter \n> ")
# column_name = input("Please what col name would you like to add \n> ")
# data_type   = input("Please enter datatype \n> ")
# qty   = input("Please input data-qty \n> ")


# with connection:
#     with connection.cursor() as cursor:
#         # Create a new record
#         sql = f"ALTER TABLE {table_name} ADD {column_name} {data_type}{f'({qty})' or qty}"

#         print("Column created..!!!")
        
#         default = input(f"Please input default value for {column_name} \n> ")
#         sql2 = f"UPDATE {table_name} set {column_name} = '{default}'"
#         print(sql2)
        
#         cursor.execute(sql)
#         cursor.execute(sql2)

#     # connection is not autocommit by default. So you must commit to save
#     # your changes.
#     connection.commit()