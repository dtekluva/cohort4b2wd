# folder = r"C:\Users\kboys\OneDrive\Desktop\CLASSES\UNIVELCITY CLASSES\cohort4b2wd\materials"

# def write_to_file( username, password):

#     file_name = "\logins.csv"
#     file = open(folder + file_name, "a")
#     file.write(f"{username},,{password}\n")

#     file.close()

# def login( username, password):

#     file_name = "\logins.csv"
#     file = open(folder + file_name, "r")
#     data = file.readlines()

#     for line in data:
#         # print(line)
#         splitted_line = line.split(",,")
#         stored_username, stored_password = splitted_line

#         if username == stored_username:
#             print("Correct username")
#             # print(password , stored_password, password == stored_password)
#             if password == stored_password.replace("\n", ""):
#                 print("correct password")
#                 print("Successfully logged in..!!!")
#         else:
#             print("Incorrect details")



# # write_to_file("ayo", "278143462")
# login("dtekluva", "qwerty")folder = r"C:\Users\kboys\OneDrive\Desktop\CLASSES\UNIVELCITY CLASSES\cohort4b2wd\materials"


import pymysql.cursors

# Connect to the database
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='',
                             database='school',
                             cursorclass=pymysql.cursors.DictCursor)

def sign_up( username, password):

    with connection.cursor() as cursor:

        sql = "INSERT INTO `users` (`username`, `password`) VALUES (%s, %s)"
        cursor.execute(sql, ({username}, {password}))

    connection.commit()

def login( username, password):

    with connection.cursor() as cursor:

        sql = "SELECT  * FROM users WHERE username = %s and password = %s;"
        cursor.execute(sql, ({username}, {password}))

        result = cursor.fetchall()

        if len(result) > 0:
            print("Login successful")
        else:
            print("Login Failed")



# sign_up("kunle", "111111")
login("kunle", "111111")