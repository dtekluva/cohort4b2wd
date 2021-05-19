numbers = input("Please enter vals with commas: ")

split_nums = numbers.split(",")
tuple_nums = tuple(split_nums)

print(split_nums, type(split_nums))
print(tuple_nums, type(tuple_nums))