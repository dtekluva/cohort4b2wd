# expr = input('write a short sentence: ')
# expr2 = expr.casefold()
# vowels = 'aeiou'
# count = 0
# for vow in expr2:

#     if vow in vowels:
#         count += 1
# print(count)

#or 

expr = input('write a short sentence: ')
expr2 = expr.casefold()
vowels = 'aeiou'
count = 0
dict_vow = {}.fromkeys(vowels,count)

for vow in expr2:

    if vow in vowels:
        # to access the value of a particular vowel as the key
        dict_vow[vow] += 1
        count += 1

print(f'TOTAL VOWEL => {count}')
print()
for vowel in dict_vow:
    print(f'{vowel} : {dict_vow[vowel]}')

