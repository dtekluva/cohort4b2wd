sentence_from_user = input('\n Welcme please enter a phrase: ')
expr2 = sentence_from_user.casefold()


vowels = 'aeiou'
dict_vow = {}
counts = 0
dict_vow[vowels] = counts
for vows in expr2:
    if vows in vowels:

        counts += 1

print(counts)


for vow, count in dict_vow.items():

    dict_vow[vow] = +1
print(f'{vow}------{count}')





