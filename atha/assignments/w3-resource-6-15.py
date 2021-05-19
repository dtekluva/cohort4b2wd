# Write a Python program which accepts a sequence of comma-separated numbers from user and generate a list and a tuple with those numbers.

# numbers = input("Please enter vals with commas: ")

# split_nums = numbers.split(",")
# tuple_nums = tuple(split_nums)

# print(split_nums, type(split_nums))
# print(tuple_nums, type(tuple_nums))

# Write a Python program to accept a filename from the user and print the extension of that. Go to the editor
# Sample filename : abc.java

# numbers = input("Please enter filename: ")
# split = numbers.split(".")
# extension = split[1]
# print(split)
# print(extension)

# import os
# target_folder = input("----> ")
# files = os.listdir(f"C:/Users/kboys/Downloads/{target_folder}")
# print(files)

# for number in range(20):
#     numbers = files[number]
#     split = numbers.split(".")
#     extension = split[-1]
#     # print(split)
#     print(extension)


# import calendar
# # x = int(input("Input the year : "))
# # y = int(input("Input the month : "))
# # print(calendar(x, y))
# print(calendar.calendar(2021))

print(help(int))
print(abs.__doc__)