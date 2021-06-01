# tenary operators  ------> <expr1> if <conditional_expr> else <expr2>



#make a list of five or more user names 


# user_names = []



# for name in user_names[:]:
    
#     if name != None:
#         print(f'Welcome {name}')
#     else:
#         print('sorry we could not find any valid us')


# requested_toppings = []
# if requested_toppings:
#     for requested_topping in requested_toppings:
#         print(f"Adding {requested_topping}.")
#         print("\nFinished making your pizza!")
#     else:
#         print("Are you sure you want a plain pizza?")


# prompt = "If you tell us who you are, we can personalize the messages you see."
# prompt += "\nWhat is your first name? "
# name = input(prompt)
# print(f"\nHello, {name}!")

# open the file in the write mode
# f = open('path/to/csv_file', 'w')

# # create the csv writer
# writer = csv.writer(f)

# # write a row to the csv file
# writer.writerow(row)

# # close the file
# f.close()


# responses = {}
# # Set a flag to indicate that polling is active.
# polling_active = True
# while polling_active:

# # Prompt for the person's name and response.

#     name = input("\nWhat is your name? ")
#     response = input("Which mountain would you like to climb someday? ")


#     # Store the response in the dictionary.
#     responses[name] = response
#     # Find out if anyone else is going to take the poll.
#     repeat = input("Would you like to let another person respond? (yes/ no) ")
#     if repeat == 'no':
#         polling_active = False
#         # Polling is complete. Show the results.
# print("\n--- Poll Results ---")
# for name, response in responses.items():
#     print(f"{name} would like to climb {response}.")
       


# from random import randint

# def random_with_N_digits(n):
#     range_start = 10**(n-1)
#     range_end = (10**n)-1
#     return randint(range_start, range_end)



# print(random_with_N_digits(6))




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


# print(f'TOTAL VOWEL => {count}')
# print()
# for vowel in dict_vow:
#     print(f'{vowel} : {dict_vow[vowel]}')



