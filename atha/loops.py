# for i in range(100):

#     for x in range(2,i):

#         if i % x == 0:

#             break
#         else:

#             continue

# else:

#     print(i)

# for i in range(1,101):
#     if i % 5 == 0:
#         print(i)


# names = ["john", "sam", "samuel", "jacob"]

# for name in names:

#     if name.startswith("s"):
#         print("Mr " + name)


# word = input("Please enter sentence : ")
# total = 0

# for char in word:
#     if char == "a":

#         total += 1

# print(total)


# while condition: 

# while True: # runs forever
#     print("Yes")
# while False: # never runs
#     print("Yes")


# i = 6

# while i < 60:

#     i+=1
#     print(i)


# i = 100

# while i >= 0:

#     # print(i)
#     i-=1

#     for x in range(2,i):

#         if i % x == 0:

#             break
#         else:

#             continue

#     else:

#         print(i)






# file_path = r"C:\Users\kboys\OneDrive\Desktop\CLASSES\UNIVELCITY CLASSES\cohort4b2wd\materials\statement2.csv"

# file = open(file_path, "r")

# data = file.readlines()

# total = 0

# for line in data:

#     splitted_lines = line.split(",")
#     # print(splitted_lines)

#     debits = splitted_lines[3]
#     credits = splitted_lines[4]
#     remarks = splitted_lines[6]
#     # print(debits)
#     # print(remarks)

#     if "Airtime" in remarks:
#         if not debits.isalnum():
#             total = total + float(debits)

# print(total)
