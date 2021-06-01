# x  = [len, print]

# x[1]("Hello world..!!")
# x[1]("Hello world..!!")

# q = x[1]

# q("Hello number 2")


# for func in x:

#     print(func("adaora"))


# names = ["ade", "kunle", "john", "sam"]

# print(names)

# names[1] = "sam"

# print(names)

# file_path = r"C:\Users\kboys\OneDrive\Desktop\CLASSES\UNIVELCITY CLASSES\cohort4b2wd\materials\gtb_doc.csv"
# file = open(file_path, "r")

# vat_deb = []

# for line in file.readlines():

#     split_line = line.split(",")
#     remarks = split_line[-1]
#     debits = split_line[3]

#     if "VALUE ADDED TAX" in remarks:
#         vat_deb.append(debits)
#         print(remarks)

# print(vat_deb)


# tuples to list speed comparison

# import timeit

# x  = timeit.timeit('"-".join(str(n) for n in tuple(range(500000)))', number=100)

# y  = timeit.timeit('"-".join(str(n) for n in list(range(500000)))', number=100)


# print(x, y)

# dicto = {}
# print(dicto)
# dicto["first val"] = "plenty"

# print(dicto)
# dicto["second val"] = "too much"

# print(dicto)

# print(dicto.get("second val"))
# print(dicto.get("third val")) # this returns none
# print(dicto.get("third val", "not found")) # this returns default value specified
# print(dicto["third val"]) # using the square bracket notation would crash with key error if key is not found.

# import requests

<<<<<<< HEAD
response = requests.get("http://datanigeria.pythonanywhere.com/play/ayo/ay123009")

data = response.json()
print(data)

=======
# # response = requests.get("https://api.publicapis.org/entries")

# # data = response.json()
# # print(data.get("count"))

# # https://pythonanywhere.com/game/ayo/ay123009'

# username = "atha"

# for number in range(100000, 999999):

#     response = requests.get(f"http://datanigeria.pythonanywhere.com/play/{username}/{number}")
#     data = response.json()

#     print("testting", number)

#     if data["status"] == True:
#         break

# IMPORT DATETIME MODULE
# import datetime

# # DEFINE FILE PATH
# file_path = r"C:\Users\kboys\OneDrive\Desktop\CLASSES\UNIVELCITY CLASSES\cohort4b2wd\materials\gtb_doc.csv"
# #
# #OPEN DEFINED FILE PATH
# file = open(file_path, "r") # 

# # CREATE EMPTY LIST IN ORDER TO PUSH VALUES FOUND FOR LATER USAGE
# vat_deb = []

# # ACCEPT KEYWORD FROM USER
# keyword = input("Please enter keyword : ")

# #  ITERATE THORUGH THE (FILE.READLINES()) I.E THE LINES READ FROM THE FILE OPENED
# for line in file.readlines():

#     # SPLIT FILE LINES INTO SECTIONS ACCORDING TO THE COMMA SEPERATION
#     split_line = line.split(",")

#     # DETERMINE THE LOCATION OF REMARKS AND OTHER COLUMNS
#     remarks = split_line[-1]
#     date = split_line[0]
#     debits = split_line[3]
#     credit = split_line[4]

#     # CHECK IF KEYWORD IS IN REMARKS AND THEN APPEND THE KEYWORD INTO THE EMPTY LIST CREATED
#     if keyword in remarks:
#         vat_deb.append(line)
#         print(remarks)

# print(vat_deb)

# #GET CURRENT DATETIME
# current_date = datetime.datetime.now()

# # FORMAT THE DATETIME AND KEYWORD INTO A STRING TO FORM A NAME FOR OUR FILE.
# new_file_name = f"{keyword}_{current_date}.csv".replace(":", "-")

# # OPEN FILE OR CREATE FILE WITH THE NAME CONSTRUCTED ABOVE 
# new_file = open(new_file_name, "w")

# # LOOP THROUGH THE VALUES WHICH HAVE BEEN APPENDED INTO THE LIST AND WRITE EACH VALUE INTO THE NEW OPENED FILE
# for line in vat_deb:
#     new_file.write(line)



# DICTIONARIES

# creating from direct notation
# friends= {
#     "Kunle": ["dancing", "singing"],
#     "sam": ["jumping", "running"],
#     "john": ["jumping", "running"],
#     "total_students": 3
# }
# print(friends)

# # creating from listof tuples
# scores = [
#     ("kunle", 54),
#     ("john", 33),
#     ("sam", 89)
# ]

# scores_dict = dict(scores)

# print(scores_dict)

# # creating via keyword arguments
# courses = dict(
#     year1 = ["math", "english"],
#     year2 = ["physics", "english"],
#     year3 = ["biology", "wave theory"]
# )

# print(courses)


# names = ["ade", "kunle", "samuel"]
# ages = [32, 45, 31]
# hobbies = ["running", "singing", "dancing"]

# # print(list(zip(names, ages, hobbies)))

# dicti = {name:[age, hobby] for name, age, hobby in zip(names, ages, hobbies)}

# print(dicti)

# x = {}
# x["boy"] = "ade"

# print(x)
# x["girl"] = "ada"
# print(x)

# sentence = input("Please enter sentence : ")
# vowels = "aeiou"

# dicti = {}

# for vowel in vowels:

#     # print(sentence.lower().count(vowel))

#     dicti[vowel] = sentence.lower().count(vowel)

# print(dicti)

# sentence = input("Please enter sentence : ")
# vowels = "aeiou"

# dicti = {vowel:sentence.lower().count(vowel) for vowel in vowels}

# print(dicti)

x = {'a': 0, 'e': 0, 'i': 3, 'o': 2, 'u': 0}
print(x["i"])# dictionaries accesed via keys
print(x["o"])# dictionaries accesed via keys
>>>>>>> 07487c42e0e7112a78a46cc4297846f390befec0
