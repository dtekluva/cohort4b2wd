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

file_path = r"C:\Users\kboys\OneDrive\Desktop\CLASSES\UNIVELCITY CLASSES\cohort4b2wd\materials\gtb_doc.csv"
file = open(file_path, "r")

vat_deb = []

for line in file.readlines():

    split_line = line.split(",")
    remarks = split_line[-1]
    debits = split_line[3]

    if "VALUE ADDED TAX" in remarks:
        vat_deb.append(debits)
        print(remarks)

print(vat_deb)