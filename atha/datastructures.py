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

import requests

response = requests.get("https://api.publicapis.org/entries")

data = response.json()
print(data.get("count"))

#https://pythonanywhere.com/game/ayo/ay123009
#https://pythonanywhere.com/game/{username}/{suggested_password}