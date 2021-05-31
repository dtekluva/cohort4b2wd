# 1. READ UP ON DICTIONARIES AND LISTS

# DICTS - https://realpython.com/python-dicts/
# LISTS - https://realpython.com/python-lists-tuples/

# 2. WRITE A PYHON PROGRAM TO TAKE IN A SENTENCE, AND THEN COUNT THE NUMBER OF OCCURENCES FOR ALL VOWELS IN THE SENTENCE.

# 3. USING EXHAUSTIVE ENUMERATION SOLVE THE IMAGE BELOW CALLED EXHAUSTIVE ENUMERATION


num_range = range(100000, 999999)

for value in num_range:
    
    if str(value)[-1]*6 == str(value*6):

        print(value)





i = 100000

while i >= 0:

    # print(i)
    i+=1

    for x in num_range:

        if i % 600000 == 0:

            break
        else:

            continue

    else:

        print(i)