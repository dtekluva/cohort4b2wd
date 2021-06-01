# expr = input('write a short sentence: ')
# expr2 = expr.casefold()
# vowels = 'aeiou'
# count = 0
# for vow in expr2:

#     if vow in vowels:
#         count += 1
# print(count)

#or 

# expr = input('write a short sentence: ')
# expr2 = expr.casefold()
# vowels = 'aeiou'
# count = 0
# dict_vow = {}.fromkeys(vowels,0)

# for vow in expr2:

#     if vow in vowels:
#         #to access the value of a particular vowel as the key
#         dict_vow[vow] += 1
#         count += 1
# print(dict_vow.__doc__)


# print(f'TOTAL VOWEL => {count}')
# print()
# for vowel in dict_vow:
#     print(f'{vowel} : {dict_vow[vowel]}')


# num_range = range(100,350)

# for value in num_range:
#     if str(value)[-1]*3 == str(value*3):
#         print(value)

# fie_path = r'/home/abayomidare/Desktop/Univelcity/cohort4b2wd/materials/gtb_doc.csv'

# open_file_path = open(fie_path, 'r')

# data = open_file_path.readline()



# data.split(',')