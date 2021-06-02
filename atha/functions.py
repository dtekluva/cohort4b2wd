# import random


# def guess():

#     computer_pick = random.randint(1,4)
#     user_pick = int(input("Please enter your guess : "))

#     if user_pick == computer_pick:
#         print("YEAAAYY")
#     else:
#         print("BOOOOO...!!!")

# for i in range(5):
#     guess()


# def journal_writer(name, title, body, date = "2021-01-01"):

#     """
#     This is one weird function that does nothing really useful.
#     """

#     file_path = r"C:\Users\kboys\OneDrive\Desktop\CLASSES\UNIVELCITY CLASSES\cohort4b2wd\materials\journal.py"
#     file = open(file_path, "a")

#     file.write(f"{name},{title},{body},{date}\n")

#     file.close()

# # journal_writer("atha", "my first journal", "This is the first journal written by a legend", "2021-01-03")
# journal_writer("atha", "my first journal", "This is the first journal written by a legend")