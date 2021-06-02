# class Employee: # BASE EMPLOYEE CLASS
#     pass

# new_employee = Employee() # instantiation
# new_employee2 = Employee() # instantiation
# new_employee4 = Employee() # instantiation
# new_employee = Employee() # instantiation
# print(new_employee)

# x = 2

# print(type(x))

# class Employee: # BASE EMPLOYEE CLASS

#     #### CLASS ATTRIBUTES ###
#     hmo_id = 132242
#     account_type = "current salary account"
#     access_code = 4563


# ade = Employee()
# print(ade.hmo_id)
# print(ade.account_type)
# kunle = Employee()
# print(kunle.hmo_id)
# print(kunle.account_type)
# print(kunle.__dir__())

# class Employee: # BASE EMPLOYEE CLASS

#     #### CLASS ATTRIBUTES ###
#     hmo_id = 132242
#     account_type = "current salary account"
#     access_code = 4563

#     #### INSTANCE ATTRIBUTES ###
#     def __init__(self, name, staff_id, salary, dept):
#         self.name = name
#         self.staff_id = staff_id
#         self.salary = salary
#         self.dept = dept


# ade = Employee("Ade Bami", 12110, 230000, "Administration")
# kunle = Employee("Samuel Bami", 21009, 100000, "Technical")

# print(ade.hmo_id)
# print(ade.account_type)
# print(ade.salary)

# print(kunle.hmo_id)
# print(kunle.account_type)
# print(kunle.salary)


# class Employee: # BASE EMPLOYEE CLASS

#     #### CLASS ATTRIBUTES ###
#     hmo_id = 132242
#     account_type = "current salary account"
#     access_code = 4563

#     #### INSTANCE ATTRIBUTES ###
#     def __init__(self, name, staff_id, salary, dept, company_name):
#         self.name = name
#         self.staff_id = staff_id
#         self.salary = salary
#         self.dept = dept
#         self.company_name = company_name

#     def describe(self):
#         print(f"""
#                 Hello my name is {self.name},
#                 and I work for {self.company_name},
#                 With a salary of {self.salary}.

#                 You can check me out, my staff id is {self.staff_id}
#                 """)

#     def __str__(self):
#         return self.name

# ade = Employee("Ade Bami", 12110, 230000, "Administration", "Toptal")
# kunle = Employee("Samuel Bami", 21009, 100000, "Technical", "KPMG")

# print(ade.describe())
# print(ade.commission)

# print(kunle.describe())
# print(str(kunle))

# class Contract_Employee(Employee):
#     commission = 0.1

#     def describe(self):
#         super().describe()
#         print(f"Also i pay a commision of {self.commission}.")

# shane = Contract_Employee("shane", 1923, 200000, "Admin", "Andela")
# shane.describe()
# print(shane.commission)

folder = r"C:\Users\kboys\OneDrive\Desktop\CLASSES\UNIVELCITY CLASSES\cohort4b2wd\materials"

def write_to_file( username, password):

    file_name = "\logins.csv"
    file = open(folder + file_name, "a")
    file.write(f"{username},,{password}\n")

    file.close()

def login( username, password):

    file_name = "\logins.csv"
    file = open(folder + file_name, "r")
    data = file.readlines()

    for line in data:
        # print(line)
        splitted_line = line.split(",,")
        stored_username, stored_password = splitted_line

        if username == stored_username:
            print("Corect username")
            # print(password , stored_password, password == stored_password)
            if password == stored_password.replace("\n", ""):
                print("correct password")
                print("Successfully logged in..!!!")
        else:
            print("Incorrect details")



# write_to_file("ayo", "278143462")
login("atha", "123456")