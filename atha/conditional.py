# import string

# x = string.ascii_lowercase() # this gives all possible characters in the alphabet.

# number = input("Enter number > ")

# if number.isnumeric():
#     print("This is a number.")
# elif number.isalpha():
#     print("This is only strings")
# elif number.isalnum():
#     print("This is mixed.")
# else:
#     print("This is not a number.")

# take full name and split into individual names
# full_name = input("Please enter you name : ")

# split_name = full_name.split(" ")

# print(split_name)

# first_name =split_name[0]
# last_name =split_name[1]

# print("First name : ", first_name)
# print("Last name : ", last_name)

dob = input("Please enter dob : ")

split_dob = dob.split("-") # split every where a - is met

year = int(split_dob[0])
print(year)

age = 2021 - year

if age >= 30:

    print("Omo you don old oo !!!")
    
else:

    print("Omo shi ni e. !!!")