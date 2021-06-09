import pymysql.cursors

# Connect to the database
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='',
                             database='school',
                             cursorclass=pymysql.cursors.DictCursor)

# with connection:
#     with connection.cursor() as cursor:
#         # Create a new record
#         sql = "INSERT INTO `student` (`stu_name`, `age`, `address`, `email`) VALUES (%s, %s, %s, %s)"
#         cursor.execute(sql, ('atha inyang', '30', '10, montgomery road, yaba.', 'inyangete@gmail.com'))

#     # connection is not autocommit by default. So you must commit to save
#     # your changes.
#     connection.commit()

# # with connection:
# with connection.cursor() as cursor:

#     # Read a single record
#     sql = "SELECT * FROM `student`"
#     cursor.execute(sql)
#     result = cursor.fetchall()
#     print(result)