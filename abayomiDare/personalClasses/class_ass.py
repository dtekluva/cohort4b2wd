# men = ['ade','john','sam']
# for man in men:
#     print(man)
# for i in range(100):
#     for x in range(2, i):
#         if i % x == 0:
#             break
#         else:
#             continue
#     else:
#         print(i)

# names = ['john','sam','samuel','jacob',]

# for name in names:
#     if name.startswith('s'):
#         print(name)


# for i in range(1, 25):
#     print(f'2 x {i} = {2 * i}')


# Iterable_mix = ['a', '5', '10', '15', '6', '7', 'c', 'd', '10']
# total = 0
# for num in Iterable_mix:
#     if num.isnumeric():
#         total = total + int(num)


# print(total)


# user_input = input('Enter a Word: ')
# total = 0

# for count in user_input:
#     if count == 'a':
#         total += 1
# print(total)

# i = 60
# while i >= 0:
#     i -= 1
#     for x in range(2, i):
#         if i % x == 0:
#             break
#         else:
#             continue
#     else:
#         print(i)

# def sum_of_number (num1, num2, num3):
#     compare = num1 == num2 == num3
#     if compare:
#         return (num1 + num2 + num3) * 3
#     else:
#         return 'try update your equation'

# print(sum_of_number(1,1,1))
# print(sum_of_number(2,1,3))

# def check(letter):
#     if len(letter) >= 2 and letter[:2] == 'is':
#         return letter
#     else:
#         return f'is {letter}'

# print(check('isGood'))
# print(check('fantastic'))

# def copies(name_name, n):
#     pp = ''
#     for i in n:
#         pp = pp + name_name

#     return pp
# print(copies('ade', 3))


# def larger_string(str, n):
#    result = ""
#    for i in range(n):
#       result = result + str
#    return result

# print(larger_string('abc', 2))
# print(larger_string('.py', 3))
