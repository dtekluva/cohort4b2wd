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

class Employee: # BASE EMPLOYEE CLASS

    #### CLASS ATTRIBUTES ###
    hmo_id = 132242
    account_type = "current salary account"
    access_code = 4563

    #### INSTANCE ATTRIBUTES ###
    def __init__(self, name, staff_id, salary, dept):
        self.name = name
        self.staff_id = staff_id
        self.salary = salary
        self.dept = dept


ade = Employee("Ade Bami", 12110, 230000, "Administration")
kunle = Employee("Samuel Bami", 21009, 100000, "Technical")

print(ade.hmo_id)
print(ade.account_type)
print(ade.salary)

print(kunle.hmo_id)
print(kunle.account_type)
print(kunle.salary)